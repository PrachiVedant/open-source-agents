from tools.calculator import calculator_tool
from tools.file_reader import file_reader_tool
from tools.current_time import current_time_tool
from tools.websearch import web_search_tool


def get_registered_tools():
	"""Return the list of registered tool callables."""
	TOOL_REGISTRY= [
		calculator_tool,
		file_reader_tool,
		current_time_tool,
		web_search_tool,
	]
	return TOOL_REGISTRY
