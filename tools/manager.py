from langchain_core.tools import tool


@tool
def hello_tool(query: str):
    """Simple hello tool for demo."""
    return f"Hello {query}!!"


class ToolManager:
    def __init__(self, config):
        self.config = config

    def get_tools(self):
        return [hello_tool]
