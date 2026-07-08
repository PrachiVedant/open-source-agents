from tools.registry import LOCAL_TOOL_REGISTRY
from backend.mcp.manager import MCPManager


class ToolManager:

    def __init__(self, config):
        self.config = config
        self.mcp_manager = MCPManager()

    async def get_tools(self):

        tool_names = self.config.get("tools", [])

        local_tools = []
        mcp_tools = []

        for tool_name in tool_names:

            if tool_name in LOCAL_TOOL_REGISTRY:
                local_tools.append(
                    LOCAL_TOOL_REGISTRY[tool_name]
                )

            else:
                try:
                    tools = await self.mcp_manager.get_adapted_tools(
                        tool_name
                    )
                    mcp_tools.extend(tools)

                except Exception:
                    raise ValueError(
                        f"Unknown tool or MCP server: {tool_name}"
                    )

        return local_tools + mcp_tools