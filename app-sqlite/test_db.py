import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# cursor.execute("SELECT id, name, price FROM products")
# rows = cursor.fetchall()

sql = "INSERT INTO PRODUCTS (NAME, PRICE) VALUES (?,?)"

cursor.execute(sql, ("Monitor", 200.0))
cursor.execute(sql, ("Laptop", 1200.0))
cursor.execute(sql, ("Headphones", 75.0))
cursor.execute(sql, ("Webcam", 60.0))
cursor.execute(sql, ("Printer", 150.0))
cursor.execute(sql, ("USB Cable", 10.0))
cursor.execute(sql, ("External HDD", 95.0))
cursor.execute(sql, ("SSD 1TB", 130.0))
cursor.execute(sql, ("Graphics Card", 650.0))
cursor.execute(sql, ("Power Supply", 110.0))

cursor.execute("SELECT id, name, price FROM products")

rows = cursor.fetchall()
conn.commit()
cursor.close()

print(rows)

