from fastapi import FastAPI
from routes.product import product
#se crea un servidor de fastapi
app = FastAPI()

app.include_router(product)

