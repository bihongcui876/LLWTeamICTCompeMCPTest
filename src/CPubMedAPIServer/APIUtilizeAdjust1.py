#@author:BHC876
import requests
import time
import json
#防止request中报错
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#基本URL 注意使用了HTTPS协议而不是上面的HTTP协议
#注意：本API组可能需要弃用众多内容
baseurl="https://cpubmed.openi.org.cn/graph/"
#用户端UA
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1000.0 Safari/537.36"
#统一请求头
headers={"User-agent":user_agent}
#bhc876的APIKey
api_key="b915f3a2cdde890c7e9eea9719edd366225a29b11d9ceb2a4407a5ca453ebe6d"

while(True):
    print("""请输入API测定指令：
    指令 | 操作
    0     退出
    1     关联三元组查询
    2     关联三元组关系
    3     医学辅助分词
    4     关系对匹配(fail)
    5     医学文献查找(fail)
    6     关联性路径匹配(fail)
    7     相似度指数(fail)
    8     （不推荐）病症推荐检查项目(fail)
    9     实体详细关系
    10    相近与相关名词
    """)
    command = input("在此处输入代号：")
    if(command=="0"):
        print("--正在退出程序--")
        break
    elif(command=="1"):
        print("--执行关联三元组查询--")
        url=baseurl+"schema"
        entity=input("输入待搜索关联实体名：")
        #测试数据：帕罗西汀，冠心病
        params={"entity":entity,"sign":api_key}
        #网络访问
        ta = time.time()
        print("正在搜索")
        response=requests.get(url=url,params=params,headers=headers,allow_redirects=False,verify=False)
        #allow_redirects用于防止链接https，本网址使用http
        #慎用verify=False，网络连接安全性很重要
        #调试点
        #print(response.json())
        #print()
        #print(response.text)
        #response.status_code()输出200表示访问成功，一般如此类数据量巨大，并非正常状况。
        #AI需要答复的一定是简单答复
        tb=time.time()
        print("搜索完毕")
        print(f"总耗时：%.5fs"%(tb-ta))
        data=response.json()
        #print(data)
        key=list(data.keys())[0]
        #print(key)
        d=data[key]
        keys=d.keys()
        print("已获得所有字段参数："+"、".join(keys))
        k=input("请输入你想访问的所有字段：").strip().split()
        if k==[]:
            continue
        else:
            for n in k:
                if n in keys:
                    output=d[n]
                    print(n+":"+str(output))
                else:
                    print(n+"不在其中")
            continue
        # 此处是处理数据输出，并且反馈有关信号的
    elif(command=="2"):
        print("--执行关联三元组信息查找--")
        idnum = input("输入待搜索关联三元组ID编号：")
        #测试数据：80260
        params = {"ID": idnum, "sign": api_key}
        url=baseurl+"triple-info"
        response = requests.get(url=url, params=params, headers=headers, allow_redirects=False, verify=False)
        #调试点
        print(response.text)
    elif(command=="3"):
        print("--执行医学分词--")
        query = input("输入有关句段：")
        # 测试数据：
        # 糖尿病大鼠血管平滑肌细胞内质网应激因子GRP78和caspase12的表达及阿托伐他汀的干预作用
        params = {"query": query, "sign": api_key}
        url = baseurl + "cut"
        response = requests.get(url=url, params=params, headers=headers, allow_redirects=False, verify=False)
        # 调试点
        print(response.text)

    elif(command=="9"):
        print("--有关名词的特别关系--")
        query1, query2 = input("输入名词与关系（空格隔开）：").strip().split()
        # 测试数据：高血压 并发症，心脏病 发病机制，库欣病 病理分型
        params = {"header": query1, "relation": query2, "sign": api_key}
        url = baseurl + "triple-sp"
        response = requests.get(url=url, params=params, headers=headers, allow_redirects=False, verify=False)
        # 调试点
        print(response.text)
    elif(command=="10"):
        print("--查找近义名词--")
        entity = input("输入一个名词：")
        # 测试数据：青光眼
        params = {"entity": entity, "sign": api_key}
        url = baseurl + "similar-entity"
        response = requests.get(url=url, params=params, headers=headers, allow_redirects=False, verify=False)
        # 调试点
        print(response.text)
        # 注意返回和示例情况不同
    else:
        print("无本指令，请重新输入。")
        continue
