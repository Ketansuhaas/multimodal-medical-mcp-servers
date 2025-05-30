from mcp.server.fastmcp import FastMCP
from tools import register_tools
from resources import register_resources
from prompts import register_prompts 

# Initialize FastMCP server
mcp = FastMCP("eeg-server")

# Register tools
register_tools(mcp)
register_resources(mcp)
register_prompts(mcp)

if __name__ == "__main__":
    mcp.run(transport='stdio')
