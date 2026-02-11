from fastapi import HTTPException, status
from app.repositories import products_repository

def get_product_by_id(product_id: int) -> int:
    
    if product_id <= 0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Invalid product id"
        )
        
    if not products_repository.product_exists(product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Product not found"
        )        
    return products_repository.get_product_by_id(product_id)

def get_products() -> list[dict]:
    return products_repository.get_all_products()

def get_products_by_max_price(max_price: float) -> list[dict]:
    
    if max_price <= 0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Invalid max price"
        )
        
    products = products_repository.get_products_by_max_price(max_price)
    
    if not products:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "No products found"
        )
    
    return products

def get_products_count() -> int:
    return products_repository.get_products_count()
    
def delete_product(product_id: int) -> None:
    
    # validamos que sea un valor valido
    if product_id <= 0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= 'Invalid product id'
        )    
    # si existe?
    if not products_repository.product_exists(product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Product not found"
        )
        
    # accion
    products_repository.delete_product(product_id)
    
def create_product(name: str, price: int ) -> int:
    
    #duplicado?
    if products_repository.product_duplicate(name):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Product with this name already exists'
        )
        
    #accion
    product_id = products_repository.create_product(name, price)
    
    return {
        "id": product_id,
        "name": name,
        "price": price
    }
    
    