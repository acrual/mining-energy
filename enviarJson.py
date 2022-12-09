import requests
import json
from frikada3 import now

# jsonData = json.dumps('dataFrame'+now+'.json')
files = {'document': open('dataFrame'+now+'.json', 'rb')}
r = requests.post("https://httpbin.org/post", files=files, headers={"Content-Type": "application/json"},)
print(r.status_code)