# FastAPI + SQLite Backend

Backend project built with **FastAPI** and **SQLite**, focused on learning
**REST API design**, **clean architecture**, and **proper separation of concerns**.

This project intentionally avoids ORMs to better understand **SQL**, **transactions**,
and **backend fundamentals at a low level**.

---

## Tech Stack
- Python 3.11
- FastAPI
- SQLite
- Uvicorn

## Project Structure

```text
app-sqlite/
├── app/
│   ├── main.py                  # FastAPI application entrypoint
│   ├── database.py              # SQLite connection handler
│   ├── core/
│   │   └── init_db.py            # Database initialization
│   ├── routes/
│   │   └── products.py           # HTTP layer (FastAPI routers)
│   ├── services/
│   │   └── products_service.py   # Business logic layer
│   └── repositories/
│       └── products_repository.py # Database access (SQL)
│
├── scripts/
│   └── seed_products.py          # Database seed scripts
│
├── tests/
│   └── test_db.py                # Tests (WIP)
│
├── docs.md
└── README.md
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