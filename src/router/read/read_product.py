import sqlite3
from fastapi import APIRouter, HTTPException, status
from database import conn 
from models.Product import Product
from typing import List


# --- Create the APIRouter instance ---
router = APIRouter(
    prefix="/read_all_Product", # All endpoints in this router will start with /Products
    tags=["read_Product"],  # Groups this router's endpoints in OpenAPI (Swagger UI)
)

@router.get("/", response_model=List[Product])
async def read_Product(sort_by_price : bool = False, sort_by_tax : bool = False):
    """
    Retrieves a specific Product by its ID.
    """
    try:
        cursor = conn.cursor()
        if sort_by_price and not sort_by_tax:
            query = "SELECT * FROM product ORDER BY price ASC"
        elif sort_by_tax and not sort_by_price:
            query = "SELECT * FROM product ORDER BY tax ASC"
        elif not sort_by_price and not sort_by_tax:
            query = "SELECT * FROM product"
        else:
            query = "SELECT * FROM product ORDER BY price tax ASC"
        
        cursor.execute(query)
        rows = cursor.fetchall() 
        if rows:
            return [Product(**row) for row in rows]
        else:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No product found."
        )
    except sqlite3.Error as e:
        print(f"Error fetching product by: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )