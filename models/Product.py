from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None  
    price: float
    tax: Optional[float] = None

