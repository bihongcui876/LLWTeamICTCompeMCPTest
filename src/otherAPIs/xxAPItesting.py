import requests

url = "https://v2.xxapi.cn/api/disease"
a=input("询问什么信息：")
params={"word":a}
payload = {}
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
    "Context-type":"application/json"
}

response = requests.get(url, headers = headers, params=params)

print(response.text)
