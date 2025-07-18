from fastapi import FastAPI
from fastmcp_server import include_fastmcp

app = FastAPI()

include_fastmcp(app)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastMCP FastAPI server!"}
