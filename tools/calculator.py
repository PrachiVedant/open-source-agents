from langchain_core.tools import tool

@tool
def calculator_tool(expression:str)->str:
    """Evaluate a mathematical expression.
    Args:
        expression (str): The mathematical expression to evaluate.
    Returns:
        str: The result of the evaluated expression.
    """
    try:
        result = eval(expression,"builtins",{})
        return str(result)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")