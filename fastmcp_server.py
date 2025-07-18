# fastmcp_server.py
# This file will contain the FastMCP server logic and integration with FastAPI.

from fastapi import FastAPI, APIRouter

# Create a router for FastMCP endpoints
fastmcp_router = APIRouter()

@fastmcp_router.get("/fastmcp/ping")
def ping():
    return {"status": "FastMCP server is running"}

# Function to include FastMCP router in a FastAPI app
def include_fastmcp(app: FastAPI):
    app.include_router(fastmcp_router)
