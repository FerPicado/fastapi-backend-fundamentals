# imports
from fastapi import APIRouter, HTTPException, status  
from database import get_connection

# POST
from pydantic import BaseModel, Field
from typing import Annotated

# main router
router = APIRouter(
    prefix='/products',
    tags=['Products']
)

@router.get('/')
def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price FROM products")
    rows = cursor.fetchall()
    conn.close()
    
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2]
        })
        
    return products
    
"""
* SQLite devuelve tuplas
* Pasamos las tuplas -> dict
* FastAPI transforma eso en JSON
"""
    
@router.get('/search')
def get_search_products(max_price: float):
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price FROM products WHERE price <= ?", (max_price,))
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        raise HTTPException(
            status_code=404,
            detail="No products found"
        )
    
    products = []
    
    for row in rows:
       products.append({ 
           "id": row[0],
           "name": row[1],
           "price": row[2]
       }) 
       
    return products

@router.get('/count')
def get_products_count():
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM products')
    row = cursor.fetchone()
    conn.close()
    
    return {
        "count": row[0]
    }
    
# POST

class ProductCreate(BaseModel):
    name: Annotated[str, Field(min_length=1, pattern=r'^[a-zA-Z0-9\s]+$')]
    price: int = Field(gt=0)
    
class ProductOut(BaseModel):
    id: int
    name: str 
    price: float
    
"""
ProductCreate -> Lo que el cliente envía
ProductOut -> Lo que el servidor devuelve
IMPORTANTE: Nunca se mezclan.
"""

@router.post('/', response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    
    try:
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verificamos duplicados
        cursor.execute('SELECT id FROM products WHERE name = ?', (product.name,))
        if cursor.fetchone():
            conn.close()
            
            raise HTTPException(
                status_code=409,
                detail='Product with this name already exists'
            )
            
        #Insert
        cursor.execute(
            'INSERT INTO products (name, price) VALUES(?,?)',
            (product.name, product.priceC)
        )
        
        # confirmar transaccion:
        conn.commit()
        
        # Obtener ID recien creado:
        new_id = cursor.lastrowid
        conn.close()
        
        # devolver lo creado:
        
        return ProductOut(
            id = new_id,
            name = product.name,
            price = product.price
        )
        
    except HTTPException: # Si el error ya es HTTP (409, 400, etc),
        #NO lo tocamos, NO lo convertimos
        raise
    
    except Exception as e:
        print(f"Logs: {e} \n")
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = 'Internal Server Error'
        )
 
@router.get('/{product_id}')
def get_product_by_id(product_id: int ):
    
    if product_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid product id")
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price FROM products WHERE id = ?", (product_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, 
                            detail="Product not found"
                            )
    
    return {
        "id": row[0], 
        "name": row[1], 
        "price": row[2]
    }

@router.delete('/{product_id}', status_code= status.HTTP_200_OK)
def delete_product(product_id: int):
    # validamos que sea un valor valido
    if product_id <= 0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= 'Invalid product id'
        )
        
    try:  
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT id FROM products WHERE id = ?',
            (product_id,)
        )   
        # si no existe 
        if cursor.fetchone() is None:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= 'Product not found'
            )   
        # si existe:
        cursor.execute(
            'DELETE FROM products WHERE id = ?',
            (product_id,)
        )
        conn.commit()
        conn.close() 
        return {"message": "Product deleted successfully"}
    
    # Si ya es una HTTPException (400, 404, 409, etc), la relanzamos sin modificarla
    except HTTPException:
        raise
    
    # Cualquier error inesperado (DB, bug, typo, etc)
    # se loguea y se responde como 500
    except Exception as e:
        print(f"Logs: {e} \n")
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= 'Internal server error'
        )