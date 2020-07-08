import requests


data = {
    "name": "TEST!"
}

ip = "http://192.168.20.177:3001/data"
requests.get(ip, params=data)
