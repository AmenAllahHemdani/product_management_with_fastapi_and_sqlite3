import sqlite3
from fastapi import APIRouter, HTTPException, status
from database import conn 
from models.Product import Product

router = APIRouter(
    prefix="/delete_Product",
    tags=["delete_Product"], 
)


@router.delete("/{Product_id}", status_code=204)  # 204 No Content
async def delete_Product(Product_id: int):
    """
    Deletes an Product.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM product WHERE id = ?", (Product_id,))
        conn.commit()
        if cursor.rowcount > 0:
            return {"message": f"Product with ID {Product_id} deleted successfully."}
        else:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"No product found with ID {Product_id} to delete."
        )
    except sqlite3.Error as e:
        print(f"Error deleting product: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error occurred while deleting the Product."
        )