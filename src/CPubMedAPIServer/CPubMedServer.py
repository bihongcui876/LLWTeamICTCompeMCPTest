from mcp.server.fastmcp import FastMCP
import logging
import time
import json
from datetime import datetime

#@author BHC876

#日志记录器
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s") #日志格式
logger=logging.getLogger(__name__)