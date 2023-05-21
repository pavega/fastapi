from fastapi import APIRouter, HTTPException
from config.db import conn, sessionmaker, SessionLocal
from models.product import ProductDB
from schemas.product import Product


product = APIRouter()

#obtiene una lista de los productos
@product.get("/products")
def get_products():
     db = SessionLocal()
     products = db.query(ProductDB).all()
     return products

#---------------------------------------
#agrega un nuevo producto
@product.post("/product")
def post_product(product: Product):
    db = SessionLocal()
    db_product = ProductDB(product_code= product.product_code,
                           available = product.available,
                           name=product.name,
                           picture=product.picture,
                           price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

#---------------------------------------
#edita la informacion de un producto
@product.put("/product/{id}")
def update_product(id: int, product: Product):
    db = SessionLocal()

    # Buscamos el producto en la base de datos
    db_product = db.query(ProductDB).filter(ProductDB.id == id).first()

    # Actualizamos los valores del producto
    db_product.product_code = product.product_code
    db_product.available = product.available
    db_product.name = product.name
    db_product.picture = product.picture
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)

    return db_product

#---------------------------------------

#obtiene un producto especifico por su ID
@product.get("/products/{id}")
def get_product(id: int):
    db = SessionLocal()

    # Buscamos el producto en la base de datos por su id
    product = db.query(ProductDB).filter(ProductDB.id == id).first()

    # Verificamos que el producto exista
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

#---------------------------------------

@product.delete("/product/{id}")
def delete_product(id: int):
    db = SessionLocal()

    # Buscamos el producto en la base de datos por su id
    product = db.query(ProductDB).filter(ProductDB.id == id).first()

    # Verificamos que el producto exista
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Eliminamos el producto de la base de datos
    db.delete(product)
    db.commit()

    return {"message": "Product successfully deleted"}