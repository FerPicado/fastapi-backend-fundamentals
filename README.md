# FastAPI + SQLite Backend

Backend project built with **FastAPI** and **SQLite**, focused on learning
**REST API design**, **clean architecture**, and **proper separation of concerns**.

This project intentionally avoids ORMs to better understand SQL, transactions,
and backend fundamentals.

---

## Tech Stack
- Python 3.11
- FastAPI
- SQLite
- Uvicorn

## Project Structure

```text
app-sqlite/
├── main.py
├── database.py
├── routes/
│   └── products.py        # HTTP layer (FastAPI routers)
├── services/
│   └── products_service.py # Business logic
├── repositories/
│   └── products_repository.py # Database access (SQL)
└── docs.md
```

## Available Endpoints

### Products
- GET /products  
- GET /products/{id}  
- GET /products/search?max_price=  
- GET /products/count
- POST /products
- DELETE /products/{id} 

## How to run
```bash
uvicorn main:app --reload
```