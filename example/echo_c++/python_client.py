import requests
import time

data={
    "message":"hello world"      
}
headers={
    
}
url="http://127.0.0.1:8000/EchoService/Echo"
while True:
    resp=requests.post(url=url,json=data)
    print(resp.text)
    time.sleep(1)
