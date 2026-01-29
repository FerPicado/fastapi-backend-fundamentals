from database import get_connection

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
    
    
     


    
    