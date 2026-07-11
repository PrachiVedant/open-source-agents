from fastapi import FastAPI

from backend.api.routes import (
    agents,
    chat,
    llms,
    tools,
    mcp,
    memory,
)

app = FastAPI(
    title="Open Source Agent Builder",
    version="1.0.0"
)

app.include_router(agents.router, prefix="/agents", tags=["Agents"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(llms.router, prefix="/llms", tags=["LLMs"])
app.include_router(tools.router, prefix="/tools", tags=["Tools"])
app.include_router(mcp.router, prefix="/mcp", tags=["MCP"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])


@app.get("/")
def health():
    return {
        "status": "running"
    }