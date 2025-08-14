from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("datetime-server")

@mcp.tool()
async def get_datetime() -> str:
    """Get the current date and time in ISO format."""
    print("get_datetime called")
    return datetime.now().isoformat()

if __name__ == "__main__":
    mcp.run(transport='stdio') 