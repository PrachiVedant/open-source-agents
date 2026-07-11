from fastapi import APIRouter
from langchain_core.messages import HumanMessage

from backend.agents.loader import AgentLoader
from backend.api.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from backend.langgraph.graph import AgentGraph

router = APIRouter()
DEFAULT_AGENT_CONFIG = AgentLoader.load("agents/sample_agent.json")


def _merge_agent_config(request_config: dict | None) -> dict:
    if not request_config:
        return dict(DEFAULT_AGENT_CONFIG)

    merged = dict(DEFAULT_AGENT_CONFIG)
    for key, value in request_config.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = {**merged[key], **value}
        else:
            merged[key] = value

    return merged


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    agent_config = _merge_agent_config(request.agent_config)

    graph = await AgentGraph(agent_config).build()

    result = await graph.ainvoke(
        {
            "messages": [HumanMessage(content=request.message)],
            "agent_config": agent_config,
        }
    )

    ai_response = result.get("messages", [])[-1].content if result.get("messages") else ""
    if not isinstance(ai_response, str):
        ai_response = str(ai_response)

    return ChatResponse(response=ai_response)