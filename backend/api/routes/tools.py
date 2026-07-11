from fastapi import APIRouter
from tools.registry import LOCAL_TOOL_REGISTRY
router=APIRouter()

@router.get("/")
def get_tools():
    return list(LOCAL_TOOL_REGISTRY.keys())
