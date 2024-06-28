from fastapi import FastAPI
from routers import contacts, users
from dependencies.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router, prefix="/api/v1")
app.include_router(contacts.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Contact Management API"}
