
import requests
import json
r = requests.request(method="GET",url="https://www.baidu.com")
print(r.text)
