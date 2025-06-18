from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Database connection
def get_db():
    conn = psycopg2.connect(
        host="db",  # <- Docker service name
        database="fastapi_db",
        user="postgres",
        password="your_secure_password",
        cursor_factory=RealDictCursor
    )
    return conn

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI & Docker!"}

@app.get("/items/")
def read_items():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return {"items": items}