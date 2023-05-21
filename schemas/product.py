from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id : Optional[int]
    product_code : str
    available : bool
    name : str
    picture : str
    price : float