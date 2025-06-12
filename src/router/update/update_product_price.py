import sqlite3
from fastapi import APIRouter, HTTPException, status, Depends
from database import conn 
from models.Product import Product

router = APIRouter(
    prefix="/Price",
    tags=["update_Product"], 
)


@router.put("/", response_model=Product)
async def update_Product_price(Product_id: int, New_Price: int):
    """
    Updates an existing Product.  The request body must contain all fields,
    even if they are unchanged.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE product SET price = ? WHERE id = ?", (New_Price, Product_id))
        conn.commit()
        if cursor.rowcount > 0:
            cursor.execute("SELECT * FROM product WHERE id = ?", (Product_id,))
            product = cursor.fetchone()
            product = Product(**product)
            return Product(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                tax=product.tax    
            )
        else:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No product found with ID {Product_id} to update."
        )
    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error occurred while update price of Product."
        )

