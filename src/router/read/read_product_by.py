import sqlite3
from fastapi import APIRouter, HTTPException, status, Query
from database import conn 
from models.Product import Product
from typing import List, Optional
import sqlite3


# --- Create the APIRouter instance ---
router = APIRouter(
    prefix="/read_Product_by", # All endpoints in this router will start with /Products
    tags=["read_Product"],  # Groups this router's endpoints in OpenAPI (Swagger UI)
)

@router.get("/", response_model=List[Product])
async def get_Products(
    # Optional query parameters for filtering
    name: Optional[str] = Query(None, description="Filter by Product name (case-insensitive partial match)"),
    description: Optional[str] = Query(None, description="Filter by Product description (case-insensitive partial match)"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price for filtering"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price for filtering"),
    tax: Optional[float] = Query(None, description="Filter by exact tax value")
):
    """
    Retrieves a list of Products, with optional filtering.
    - If no filters are provided, all Products are returned.
    - Filters can be applied by name, description (partial, case-insensitive match),
      price range (min_price, max_price), and exact tax value.
    """
    query_parts = [] # Stores conditions for the WHERE clause
    query_values = [] # Stores values to bind to the query placeholders

    # Build the WHERE clause dynamically based on provided query parameters
    if name:
        query_parts.append("name LIKE ?")
        query_values.append(f"%{name}%") # Add '%' for partial match
    if description:
        query_parts.append("description LIKE ?")
        query_values.append(f"%{description}%") # Add '%' for partial match
    if min_price is not None: # Use 'is not None' because 0.0 is a valid value
        query_parts.append("price >= ?")
        query_values.append(min_price)
    if max_price is not None:
        query_parts.append("price <= ?")
        query_values.append(max_price)
    if tax is not None:
        query_parts.append("tax = ?")
        query_values.append(tax)

    # Construct the base query
    base_query = "SELECT id, name, description, price, tax FROM product"

    # Add WHERE clause if filters are present
    if query_parts:
        full_query = f"{base_query} WHERE {' AND '.join(query_parts)}"
    else:
        full_query = base_query # No filters, select all

    try:
        cursor = conn.cursor()
        cursor.execute(full_query, tuple(query_values)) # Execute with dynamic query and values
        rows = cursor.fetchall() # Fetch all matching rows

        # Convert sqlite3.Row objects (which behave like dictionaries) to Pydantic Product models
        Products = [Product(**row) for row in rows]
        return Products

    except sqlite3.Error as e:
        print(f"Database error during Product retrieval: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal server error occurred while retrieving Products."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )