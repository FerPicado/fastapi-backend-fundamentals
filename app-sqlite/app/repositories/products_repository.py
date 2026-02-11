from app.database import get_connection

def product_exists(product_id: int) -> bool:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT 1 FROM products WHERE id = ?",
        (product_id,)
    )
    
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def get_all_products() -> list[dict]:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price FROM products")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {"id": row[0], "name": row[1], "price": row[2]}
        for row in rows
    ]
    
def get_products_by_max_price(max_price: float) -> list[dict]:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price FROM products WHERE price <= ?", (max_price,))
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            "id": row[0],
            "name": row[1],
            "price": row[2]
        }
        for row in rows
    ]
    
def get_product_by_id(product_id: int) -> int:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price FROM products WHERE id = ?", (product_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    return {        
        "id": row[0],
        "name": row[1],
        "price": row[2]
    }
        
def get_products_count() -> int:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM products')
    row = cursor.fetchone()
    conn.close()
    
    return {
        "count": row[0]
    }
    
def delete_product(product_id: int) -> None:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "DELETE FROM products WHERE ID = ?",
        (product_id,)
    )
    
    conn.commit()
    conn.close()



def create_product(name: str, price: int) -> int:
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO products (name, price) VALUES(?,?)',
        (name, price)
    )
    
    conn.commit()
    
    new_id = cursor.lastrowid
    conn.close()
    
    return new_id

def product_duplicate(name: str) -> bool: 
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT 1 FROM products WHERE name = ?",
        (name,)
    )
        
    result = cursor.fetchone() is not None
    conn.close()
    
    return result
    
    
     


    
    