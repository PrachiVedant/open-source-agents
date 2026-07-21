from fastapi import APIRouter, HTTPException

from backend.database.crud import AgentRepository
from backend.database.schemas import AgentCreate

router = APIRouter()

repo = AgentRepository()


@router.get("/")
def list_agents():
    return repo.list()


@router.get("/{agent_id}")
def get_agent(agent_id: int):
    agent = repo.get(agent_id)

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    return agent


@router.post("/")
def create_agent(agent: AgentCreate):
    return repo.create(
        name=agent.name,
        description=agent.description,
        config=agent.config,
    )


@router.put("/{agent_id}")
def update_agent(agent_id: int, agent: AgentCreate):
    updated = repo.update(
        name=agent.name,
        config=agent.config,
        description=agent.description,
        agent_id=agent_id,
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Agent not found")

    return updated


@router.delete("/{agent_id}")
def delete_agent(agent_id: int):
    deleted = repo.delete(
        name=None,
        config=None,
        description=None,
        agent_id=agent_id,
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Agent not found")

    return {"message": "Agent deleted successfully"}