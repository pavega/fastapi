from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Text, Boolean, String, Float
from config.db import meta , engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Definir el modelo de la tabla products
class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_code = Column(String(500))
    available = Column(Boolean)
    name = Column(String(500))
    picture = Column(String(500))
    price = Column(Float)



