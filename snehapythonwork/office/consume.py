from urllib import response
import requests

response = requests.get('127.0.0.1:8000/office')
print(response.json)