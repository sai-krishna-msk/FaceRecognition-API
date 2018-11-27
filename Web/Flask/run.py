import requests
import base64
import json


data=""
with open("test.jpg" , 'rb') as f:
    data = f.read()

image = base64.b64encode(data)


result = requests.post(" https://da4358df.ngrok.io/ec/python/test", data=image)
print(result.text)
