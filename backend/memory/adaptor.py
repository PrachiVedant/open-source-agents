import asyncio
from typing import Any

from langchain_core.tools import BaseTool
from pydantic import Field

class MCPAdaptorTool(BaseTool):
    """Adapts MCP Tool to Langchain BaseTool."""

    tool:Any
    client:Any=Field(exclude=True)

    @property
    def name(self)->str:
        return self.tool.name
    
    @property
    def description(self)->str:
        return self.tool.description
    
    def _run(self,**kwargs):
        """
        Synchronous wrapper around the async MCP tool call.
        """
        return asyncio.run(self._arun(**kwargs))
    
    async def _arun(self,**kwargs):
        """Execute the tool."""
        result=await self.client.call_tool(
            tool_name=self.tool.name,
            args=kwargs
        )
        return result