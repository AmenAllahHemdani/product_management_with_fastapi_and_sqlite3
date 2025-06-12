import sqlite3
from fastapi import APIRouter, HTTPException, status
from database import conn 
from models.Product import Product


router = APIRouter(
    prefix="/add_Product",
    tags=["Products"], 
)

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def add_Product(Product: Product):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO product (id, name, description, price, tax) VALUES (?, ?, ?, ?, ?)",
            (Product.id, Product.name, Product.description, Product.price, Product.tax)
        )
        conn.commit()
        return Product

    except sqlite3.IntegrityError:
        # If a UNIQUE constraint is violated (e.g., duplicate ID if ID is PRIMARY KEY)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Product with ID '{Product.id}' already exists."
        )
    except sqlite3.Error as e:
        # Catch any other SQLite-specific errors
        print(f"SQLite error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error occurred while creating the Product."
        )
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}") # Log for debugging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )
