

import requests


base_url = "http://47.98.197.101/tzg-rest"
read_url =  ""
method = ""
params = ""
url = base_url + read_url
headers = ""
resp = requests.request(method = method,url = url,params = params,headers = headers)
# respJson =  resp.json()