from fastapi import FastAPI

from src.router.add import add_product
from src.router.read import read_product_by, read_product_by_id ,read_product
from src.router.update import update_product_price ,update_product_tax, update_product_description, update_product_name
from src.router.delete import delete_product


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Product API!"}


app.include_router(add_product.router) 

app.include_router(read_product.router)
app.include_router(read_product_by.router)
app.include_router(read_product_by_id.router)

app.include_router(update_product_name.router)
app.include_router(update_product_description.router)
app.include_router(update_product_price.router)
app.include_router(update_product_tax.router)

app.include_router(delete_product.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)