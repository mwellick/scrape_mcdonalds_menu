import json
from fastapi import FastAPI, HTTPException
from starlette import status

with open("nutrients_data.json", encoding="utf-8") as f:
    products = json.load(f)

app = FastAPI(docs_url="/", title="McDonalds Menu")


@app.get("/all_products/", status_code=status.HTTP_200_OK)
async def get_all_products():
    return products


@app.get("/products/{product_name}", status_code=status.HTTP_200_OK)
async def get_specific_product(product_name: str):
    for product in products:
        if product_name.lower() in product["name"].lower():
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@app.get("/products/{product_name}/{product_field}/", status_code=status.HTTP_200_OK)
async def retrieve_specific_product_field(product_name: str, product_field: str):
    for product in products:
        if product_name.lower() in product["name"].lower():
            if product_field in product:
                return product[product_field]
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"This {product_field} not found in this product"
                )

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
