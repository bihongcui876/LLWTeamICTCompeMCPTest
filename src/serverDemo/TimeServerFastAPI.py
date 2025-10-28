# 暂时不使用
from fastapi import FastAPI,Request

# 此处FastAPI-MCP需要使用0.1.8才可以使用add_mcp_server
# pip install fastmcp-api==0.1.8，其他版本可能是FastApiMCP
from fastapi_mcp import add_mcp_server
from typing import Any
import fastapi_mcp
import httpx
import json
import sys
import os
import uvicorn
import datetime
import time
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette import EventSourceResponse


# 应用实例化
app=FastAPI()
# server
server=add_mcp_server(
    app, # FastAPI应用
    mount_path="/mcp",
    name="current-time",
    describe_all_responses=True, #默认False，相当于把所有可能的响应模式都包含在工具描述中。
    describe_full_response_schema=True, #默认False，相当于JSON模式包含在工具描述。
)


@server.tool(name="currentTime",description="获取当前时间")
@app.get("/current-time")
async def current_time()->str:
    formatted_time=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    return formatted_time

app.add_middleware(
    CORSMiddleware,
    allow_orgins=["*"],
    allow_credientials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# 保证前端访问正常

@app.get("/stream")
async def message_stream(request:Request):
    async def event_generator():
        while True:
            # 断联反馈
            if await request.is_disconnected():
                break
            # 生成数据
            data_to_send=time.time()
            yield {"data":data_to_send}
            # 间隔迭代
            await asyncio.sleep(1)
    return EventSourceResponse(event_generator())

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)