from fastapi import FastAPI, HTTPException, status, Request
from pydantic import BaseModel
import requests

app = FastAPI()

# Get route for a simple "Hello, World!" test message
@app.get('/')
def hello_world():
    return {'message': 'Hello, World!'}

# Running the FastAPI app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
