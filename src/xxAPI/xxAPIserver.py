#
#
#   TESTING SUCCEED!!!!!!!!!!!!!!
#
#   測 試 成 功
#
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
import json
import requests

mcp=FastMCP("xxAPIServer")

def searchfor(query:str):
    url = "https://v2.xxapi.cn/api/disease"
    params = {"word": query}
    payload = {}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
        "Context-type": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    # print(response.text)
    table = response.json()
    data = table["data"]
    return data

# detail
@mcp.tool(name="ill_search_detail",description="输入病症，反馈十分详细的有关信息")
def search_detail(query:str):
    """
    获取病症详情信息。
    Args:
        query(str): 是一个病症的名称，当涉及此或此类病症时，可以输入此名称
    Return:
        output: 一个包含各种病症十分详细信息列表(dict格式)的数组，使用json包装
    """
    data = searchfor(query)
    if(data):
        return json.dumps(data, ensure_ascii=False)
    else:
        return {"result":"not found"}

# normal(simple)
@mcp.tool(name="ill_search",description="输入病症，获得有关信息")
def search_normal(query:str):
    """
    获取病症常规信息。
    Args:
        query(str): 是一个病症的名称，当涉及此或此类病症时，可以输入此名称
    Return:
        output: 一个包含各种病症信息列表(dict格式)的数组，使用json包装
    """
    data=searchfor(query)
    if data:
        output=[]
        for i in data:
            d = {}
            d["name"] = i["name"]
            d["acompany"] = i["acompany"]
            d["category"] = i["category"]
            d["cause"] = i["cause"]
            d["check"] = i["check"]
            d["cure_department"] = i["cure_department"]
            d["cure_lasttime"] = i["cure_lasttime"]
            d["cured_prob"] = i["cured_prob"]
            d["desc"] = i["desc"]
            d["get_way"] = i["get_way"]
            d["prevent"] = i["prevent"]
            d["recommand_drug"] = i["recommand_drug"]
            d["yibao_status"] = i["yibao_status"]
            output.append(d)
        return json.dumps(output, ensure_ascii=False)
    else:
        return "not found"

# simple(less)
@mcp.tool(name="ill_search_simple",description="输入病症，获得精练信息")
def search_simple(query:str):
    """
    获取病症精练信息。
    Args:
        query(str): 是一个病症的名称，当涉及此或此类病症时，可以输入此名称
    Return:
        output: 一个包含各种病症信息列表(dict格式)的数组，使用json包装
    """
    data=searchfor(query)
    if data:
        output=[]
        for i in data:
            d = {}
            d["name"] = i["name"]
            d["category"] = i["category"]
            d["cause"] = i["cause"]
            d["check"] = i["check"]
            d["cure_department"] = i["cure_department"]
            d["desc"] = i["desc"]
            d["get_way"] = i["get_way"]
            d["prevent"] = i["prevent"]
            d["recommand_drug"] = i["recommand_drug"]
            d["yibao_status"] = i["yibao_status"]
            output.append(d)
        return json.dumps(output, ensure_ascii=False)
    else:
        return "not found"

# description
@mcp.tool(name="ill_search_description",description="输入病症，获得描述信息")
def search_desc(query:str):
    """
    获取病症常规信息。
    Args:
        query(str): 是一个病症的名称，当涉及此或此类病症时，可以输入此名称
    Return:
        result: 一个包含各种病症信息列表(dict格式)的数组，使用json包装
    """
    data=searchfor(query)
    if data:
        output=[]
        for i in data:
            d = {}
            d["name"] = i["name"]
            d["category"] = i["category"]
            d["cause"] = i["cause"]
            d["check"] = i["check"]
            d["desc"] = i["desc"]
            d["get_way"] = i["get_way"]
            d["prevent"] = i["prevent"]
            d["recommand_drug"] = i["recommand_drug"]
            output.append(d)
        return json.dumps(output, ensure_ascii=False)
    else:
        return "not found"

# medicine
@mcp.tool(name="ill_search_detail_medicine",description="输入病症，获得全部有关药物")
def search_medicine(query:str):
    """
    获取病症常规信息。
    Args:
        query(str): 是一个病症的名称，当涉及此或此类病症时，可以输入此名称
    Return:
        result: 一个包含各种病症信息列表(dict格式)的数组，使用json包装
    """
    data=searchfor(query)
    if data:
        output=[]
        for i in data:
            d = {}
            d["name"] = i["name"]
            d["check"] = i["check"]
            d["drug_detail"] = i["drug_detail"]
            d["yibao_status"] = i["yibao_status"]
            output.append(d)
        return json.dumps(output, ensure_ascii=False)
    else:
        return "not found"

# list
@mcp.tool(name="ill_search_list",description="输入病症，获得全部名称与分类列表")
def search_simple(query:str):
    """
    获取病症常规信息。
    Args:
        query(str): 是一个病症的名称，当涉及此或此类病症时，可以输入此名称
    Return:
        result: 一个包含各种病症信息列表(dict格式)的数组，使用json包装
    """
    data=searchfor(query)
    if data:
        output=[]
        for i in data:
            d = {}
            d["name"] = i["name"]
            d["category"] = i["category"]
            output.append(d)
        return json.dumps(output, ensure_ascii=False)
    else:
        return "not found"

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

    uvicorn.run(app,host="127.0.0.1",port=9090)