from langchain_core.tools import tool

@tool
def file_reader_tool(path:str)->str:
    """Read the contents of a file.
    Args:
        path (str): The path to the file to read.
    Returns:
        str: The contents of the file.
    """
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")
    
   