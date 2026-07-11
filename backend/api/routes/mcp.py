from fastapi import APIRouter

from backend.mcp.config import MCP_SERVERS

router = APIRouter()


@router.get("/")
def get_mcp():
    return list(MCP_SERVERS.keys())
