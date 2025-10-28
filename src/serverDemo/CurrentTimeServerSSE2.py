import httpx
from mcp.server.fastmcp import FastMCP
from datetime import datetime

mcp=FastMCP("currentTime")

@mcp.tool(name="current_time",description="获取本机当前时间")
async def current_time()->str:
    ct=datetime.now()
    ftime=ct.strftime("%Y-%m-%dT%H:%M:%S")
    return ftime

if __name__ == "__main__":
    mcp.run(transport="sse")