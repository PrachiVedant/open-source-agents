from langchain_core.tools import tool
from tools.registry import TOOL_REGISTRY


class ToolManager:
    def __init__(self, config):
        self.config = config

    def get_tools(self):
        tools_names=self.config.get("tools", [])
        tools = []
        for tool_name in tools_names:
            if tool_name not in TOOL_REGISTRY:
                raise ValueError(f"Tool '{tool_name}' is not registered.")
            tools.append(TOOL_REGISTRY[tool_name])
        return tools
