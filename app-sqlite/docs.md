conn = sqlite3.connect("products.db")   # abro llamada
cursor = conn.cursor()                  # alguien que ejecute SQL
cursor.execute("INSERT INTO products VALUES (...)")  # hago cambios
conn.commit()                            # confirmo los cambios
conn.close()                             # cuelgo


SQLite devuelve listas de tuplas

Cada fila es una tupla

El backend no trabaja directo con JSON

Vos transformás datos → JSON después

Esto es clave mental.

## El router NO piensa.
## El router delega.

```text
El router:

recibe parámetros

llama a un service

devuelve respuesta

Nada más.
```