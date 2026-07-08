from tools.calculator import calculator_tool
from tools.file_reader import file_reader_tool
from tools.current_time import current_time_tool
from tools.websearch import web_search_tool


LOCAL_TOOL_REGISTRY = {
    "calculator": calculator_tool,
    "calculator_tool": calculator_tool,
    "file_reader": file_reader_tool,
    "file_reader_tool": file_reader_tool,
    "current_time": current_time_tool,
    "current_time_tool": current_time_tool,
    "websearch": web_search_tool,
    "web_search_tool": web_search_tool,
}


def get_registered_tools():
    """Return the list of registered tool callables."""
    return LOCAL_TOOL_REGISTRY
