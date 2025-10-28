from datetime import datetime

from mcp.types import Tool, TextContent
from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from starlette.responses import Response
from starlette.routing import Route
import httpx
import mcp.server.stdio
import uvicorn
import logging

#工具说明
tools=Tool(name="current_time",description="获取本地实时时间",inputSchema={})
#样例MCP server测试

#logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
#logger=logging.getLogger(__name__)

def current_time()->list[TextContent]:
    current = datetime.now()
    # 格式化
    fmttm = current.strftime("%Y-%m-%dT%H:%M:%S")
    # 日志
    #logger.info("formatted current time: %s", fmttm)
    # 返回
    return [TextContent(type="text",text=fmttm)]

server=Server("current-time")

@server.list_tools()
async def list_tools():
    return [tools]

@server.call_tool()
async def call_tool(name:str):
    if name == "current-time":
        return await current_time()
    raise ValueError(f"Unknown tool: {name}")

sse=SseServerTransport("/messages/")

async def handle_sse(request):
    async with sse.connect_sse(request.scope,request.receive,request._send) as streams:
        await server.run(streams[0],streams[1],server.create_initialization_options())
    return Response()

app=Starlette(
    debug=True,
    routes=[Route("/sse",endpoint=handle_sse,methods=["GET"]),Mount("/messages/",app=sse.handle_post_message)]
)

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)