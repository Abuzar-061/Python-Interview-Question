# Run Command :=> uvicorn filename:initializer_name
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"mesasge": "Hello! My name is Abuzar, What about your's ?"}