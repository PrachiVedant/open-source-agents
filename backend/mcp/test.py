import asyncio

from backend.mcp.client import MCPClient
from backend.mcp.config import MCP_SERVERS


async def main():

    client = MCPClient(
        MCP_SERVERS["filesystem"]
    )

    tools = await client.list_tools()

    print("\nAvailable MCP Tools:\n")

    for tool in tools:
        print(tool.name)


asyncio.run(main())