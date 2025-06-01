from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/status")
def get_status():
    return {"status": "ok"}

@app.get("/users")
def list_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.post("/users")
def create_user():
    return JSONResponse(content={"message": "User created (dummy)"}, status_code=201)

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "description": "Dummy item"}

def main():
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
