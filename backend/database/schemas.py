from pydantic import BaseModel


class AgentCreate(BaseModel):
    name: str
    description: str | None = None
    config: dict