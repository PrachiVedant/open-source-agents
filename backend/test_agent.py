import sys
from pathlib import Path

from langchain_core.messages import HumanMessage

ROOT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = str(Path(__file__).resolve().parent)

if BACKEND_DIR in sys.path:
    sys.path.remove(BACKEND_DIR)

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.agents.loader import AgentLoader
from backend.langgraph.graph import AgentGraph

# Load config
config = AgentLoader.load("agents/sample_agent.json")

# Build graph
graph = AgentGraph(config).build()

# Invoke graph
response = graph.invoke(
    {
        "messages": [
            HumanMessage(content="Say Hello using the hello_tool!"),
        ],
        "agent_config": config,
    }
)

print(response["messages"][-1].content)