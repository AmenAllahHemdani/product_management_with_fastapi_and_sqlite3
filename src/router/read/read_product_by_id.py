import sqlite3
from fastapi import APIRouter, HTTPException, status
from database import conn 
from models.Product import Product


# --- Create the APIRouter instance ---
router = APIRouter(
    prefix="/read_Product_by_id", # All endpoints in this router will start with /Products
    tags=["read_Product"],  # Groups this router's endpoints in OpenAPI (Swagger UI)
)

@router.get("/{Product_id}", response_model=Product)
async def read_Product_by_id(Product_id: int):
    """
    Retrieves a specific Product by its ID.
    """
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM product WHERE id = ?"
        cursor.execute(query, (Product_id,))
        user = cursor.fetchone() # Fetch single row
        if user:
            user = Product(**user)
            return Product(
                id=user.id,
                name=user.name,
                description=user.description,
                price=user.price,
                tax=user.tax    
            )
        else:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No product found with id '{Product_id}'."
        )
    except sqlite3.Error as e:
        print(f"Error fetching product by {item}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )