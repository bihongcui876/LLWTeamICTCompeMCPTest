import requests
import time
import json
import asyncio
import httpx

# 本此更改的重点在于处理有关输出量，使得不要一直输出那么多。分为四五个品种

flag=True
while(flag):
    url = "https://v2.xxapi.cn/api/disease"
    a=input("询问什么信息（输入-1退出）：")
    if a=="-1":
        print("正在退出")
        flag=False
        break
    else:
        params={"word":a}
        payload = {}
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
            "Context-type":"application/json"
        }
        response = requests.get(url, headers = headers, params=params)
        #print(response.text)
        table=response.json()
        data=table["data"]
        # output trying
        if data:
            cmd=input("""输出的详细程度（输入前缀数字）：
            0.（不输入默认为0）全部输出
            1.一般输出
            2.少量信息
            3.描述特色
            4.药物汇集
            5.检索所得项目
            输入数字：
            """)
            output=[]
            if cmd=="1":#simple
                for i in data:
                    d={}
                    d["name"]=i["name"]
                    d["acompany"]=i["acompany"]
                    d["category"]=i["category"]
                    d["cause"]=i["cause"]
                    d["check"]=i["check"]
                    d["cure_department"]=i["cure_department"]
                    d["cure_lasttime"]=i["cure_lasttime"]
                    d["cured_prob"]=i["cured_prob"]
                    d["desc"]=i["desc"]
                    d["get_way"]=i["get_way"]
                    d["prevent"]=i["prevent"]
                    d["recommand_drug"]=i["recommand_drug"]
                    d["yibao_status"]=i["yibao_status"]
                    output.append(d)
                print(json.dumps(output,ensure_ascii=False))
            elif cmd=="2":#less
                for i in data:
                    d={}
                    d["name"]=i["name"]
                    d["category"]=i["category"]
                    d["cause"]=i["cause"]
                    d["check"]=i["check"]
                    d["cure_department"]=i["cure_department"]
                    d["desc"]=i["desc"]
                    d["get_way"]=i["get_way"]
                    d["prevent"]=i["prevent"]
                    d["recommand_drug"]=i["recommand_drug"]
                    d["yibao_status"]=i["yibao_status"]
                    output.append(d)
                print(json.dumps(output,ensure_ascii=False))
            elif cmd=="3":#desciption
                for i in data:
                    d={}
                    d["name"]=i["name"]
                    d["category"]=i["category"]
                    d["cause"]=i["cause"]
                    d["check"]=i["check"]
                    d["desc"]=i["desc"]
                    d["get_way"]=i["get_way"]
                    d["prevent"]=i["prevent"]
                    d["recommand_drug"]=i["recommand_drug"]
                    output.append(d)
                print(json.dumps(output,ensure_ascii=False))
            elif cmd=="4":
                for i in data:
                    d={}
                    d["name"]=i["name"]
                    d["category"]=i["category"]
                    d["check"]=i["check"]
                    d["drug_detail"]=i["detail"]
                    d["yibao_status"]=i["yibao_status"]
                    output.append(d)
                print(json.dumps(output,ensure_ascii=False))
            elif cmd=="5":
                for i in data:
                    d={}
                    d["name"]=i["name"]
                    d["category"]=i["category"]
                    d["yibao_status"]=i["yibao_status"]
                    output.append(d)
                print(json.dumps(output,ensure_ascii=False))
            else:
                print(json.dumps(data,ensure_ascii=False))
        else:
            print("not found")
            continue



