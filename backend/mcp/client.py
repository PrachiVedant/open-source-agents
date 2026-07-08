from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
class MCPClient:
    def __init__(self,server_config):
        self.server_config=server_config
    
    async def list_tools(self):
        params=StdioServerParameters(
            command=self.server_config["command"],
            args=self.server_config["args"]
        )
        async with stdio_client(params) as (read,write):
            async with ClientSession(read,write) as session:
                await session.initialize()
                tools=await session.list_tools()
                return tools.tools
    

    async def call_tool(self, tool_name: str, arguments: dict):

        params = StdioServerParameters(
            command=self.server_config["command"],
            args=self.server_config["args"]
        )

        async with stdio_client(params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.call_tool(
                    tool_name,
                    arguments=arguments
                )

                return result