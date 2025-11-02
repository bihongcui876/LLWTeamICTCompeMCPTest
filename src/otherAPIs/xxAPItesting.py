import requests

url = "https://v2.xxapi.cn/api/disease?word=咳嗽变异性哮喘"

payload = {}
headers = {
    'User-Agent': 'xiaoxiaoapi/1.0.0'
}

response = requests.get(url, headers = headers, data = payload)

print(response.text)
