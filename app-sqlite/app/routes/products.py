# imports
from fastapi import APIRouter, status  
from app.services import products_service

# POST
from pydantic import BaseModel, Field
from typing import Annotated

# main router
router = APIRouter(
    prefix='/products',
    tags=['Products']
)

@router.get('/')
def get_products_endpoint():
    return products_service.get_products()

@router.get('/search')
def get_search_products(max_price: float):
    return products_service.get_products_by_max_price(max_price)
    

@router.get('/count')
def get_products_count():
    return products_service.get_products_count()
    
# POST

class ProductCreate(BaseModel):
    name: Annotated[str, Field(min_length=1, pattern=r'^[a-zA-Z0-9\s]+$')]
    price: float = Field(gt=0)
    
class ProductOut(BaseModel):
    id: int
    name: str 
    price: float
    
"""
ProductCreate -> Lo que el cliente envía
ProductOut -> Lo que el servidor devuelve
IMPORTANTE: Nunca se mezclan.
"""

@router.post('/', response_model=ProductOut)
def create_product_endpoint(product: ProductCreate):
    
    return products_service.create_product(
        name=product.name,
        price=product.price
    )

@router.get('/{product_id}')
def get_product_by_id(product_id: int ):
    return products_service.get_product_by_id(product_id)

@router.delete('/{product_id}', status_code= status.HTTP_200_OK)
def delete_product_endpoint(product_id: int):
    products_service.delete_product(product_id)    
    return {"message": "Product deleted successfully"}
