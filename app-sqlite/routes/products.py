# imports
from fastapi import APIRouter, HTTPException, status
from database import get_connection


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