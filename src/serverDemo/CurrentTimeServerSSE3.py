import uvicorn
import datetime
import time
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request
# import logging

# 配置日志
# logging.basicConfig(level=logging.INFO)
# logger=logging.getLogger(__name__)

# 初始化mcp服务器
mcp=FastMCP("current-time")

# 工具
@mcp.tool(name="current_time",description="获取本地实时时间")
def current_time()->str:
    formatted_time=datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    return formatted_time

@mcp.tool(name="get_timestamp",description="获取当前时间戳")
def get_timestamp()->int:
    return int(time.time())

sse_transport = SseServerTransport("/messages/")

async def sse_handler(request):
    # logger.info(f"SSE connection established from {request.client.host}")
    async with sse_transport.connect_sse(request.scope,request.receive,request._send) as streams:
        await mcp._mcp_server.run(streams[0],streams[1],mcp._mcp_server.create_initialization_options())

async def health_check(request:Request):
    return JSONResponse({
        "status":"healthy",
        "service":"current-time-mcp",
        "timestamp":time.time()
    })

# 根端点
async def root(request:Request):
    return JSONResponse({
        "message":"MCP server is running",
        "endpoints":{
            "sse":"/sse",
            "health":"/health",
            "messages":"/messages/"
        }
    })

app=Starlette(
    debug=True,
    routes=[
        Route("/",endpoint=root,methods=["GET"]),
        Route("/sse",endpoint=sse_handler,methods=["GET"]),
        Route("/health",endpoint=health_check,methods=["GET","POST"]),
        Mount("/messages/",app=sse_transport.handle_post_message)
    ]
)

# CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应该限制为具体域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],
)

# 405错误处理
@app.exception_handler(405)
async def method_not_allowed_handler(request: Request, exc: Exception):
    """处理 405 错误"""
    # logger.warning(f"Method not allowed: {request.method} {request.url}")
    return JSONResponse(
        status_code=405,
        content={
            "error": "MethodNotAllowed",
            "message": f"Method {request.method} not allowed for {request.url.path}",
            "allowed_methods": ["GET", "POST"]  # 根据实际端点调整
        }
)
# 404错误处理
@app.exception_handler(404)
async def not_found_handler(request: Request, exc: Exception):
    """处理 404 错误"""
    return JSONResponse(
        status_code=404,
        content={
            "error": "NotFound",
            "message": f"Endpoint {request.url.path} not found",
            "available_endpoints": ["/", "/sse", "/health", "/messages/"]
        }
    )

if __name__=="__main__":

    uvicorn.run(app,host="127.0.0.1",port=8000)