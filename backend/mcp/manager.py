from typing import Any

from langchain_core.tools import BaseTool
from pydantic import Field

from backend.mcp.client import MCPClient
from backend.mcp.config import MCP_SERVERS


class MCPToolAdapter(BaseTool):
    """
    Adapts an MCP tool into a LangChain BaseTool.
    """

    name: str
    description: str

    tool: Any
    client: MCPClient = Field(exclude=True)

    model_config = {
        "arbitrary_types_allowed": True
    }

    def _format_result(self, result: Any) -> str:
        if hasattr(result, "content"):
            texts = []

            for item in result.content:
                if hasattr(item, "text"):
                    texts.append(item.text)
                else:
                    texts.append(str(item))

            return "\n".join(texts)

        return str(result)

    def _run(self, **kwargs):
        raise NotImplementedError(
            "MCP tools support async execution only."
        )

    async def _arun(self, **kwargs):

        result = await self.client.call_tool(
            tool_name=self.name,
            arguments=kwargs
        )

        return self._format_result(result)


class MCPManager:

    def __init__(self):
        self.clients = {}

    def get_client(self, server_name: str) -> MCPClient:

        if server_name not in self.clients:

            self.clients[server_name] = MCPClient(
                MCP_SERVERS[server_name]
            )

        return self.clients[server_name]

    async def get_adapted_tools(self, server_name: str):

        client = self.get_client(server_name)

        tools = await client.list_tools()

        return [
            MCPToolAdapter(
                name=tool.name,
                description=tool.description,
                tool=tool,
                client=client
            )
            for tool in tools
        ]