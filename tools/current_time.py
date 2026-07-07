from langchain_core.tools import tool
from datetime import datetime
@tool
def current_time_tool(time:str)->str:
    """
    Get the current time.
    Args:
        time (str): The time to return.
    Returns:
        str: The current time.
    """
    try:
        now=datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise ValueError(f"Error getting current time: {e}")
   