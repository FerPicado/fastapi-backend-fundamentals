# FastAPI + SQLite Backend

Small backend project built with FastAPI and SQLite to practice REST APIs and database integration.

## Tech Stack
- Python 3.11
- FastAPI
- SQLite
- Uvicorn

## Project Structure

app-sqlite/
├── main.py
├── database.py
└── routes/
    └── products.py

## Available Endpoints

### Products
- GET /products  
- GET /products/{id}  
- GET /products/search?max_price=  
- GET /products/count  

## How to run
```bash
uvicorn main:app --reload
