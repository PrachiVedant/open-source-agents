from fastapi import APIRouter

from backend.memory.in_memory import InMemory

router = APIRouter()


@router.get("/")
def get_memory():
    memory = InMemory()
    return {"status": "ok", "memory": memory.memory}
