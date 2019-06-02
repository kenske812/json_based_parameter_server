# coding: utf-8


import json
import urllib.request


url = "http://localhost:8083/do-the-work"

data = {
    "id": 8,
    "filename": "fig.png",
    "exposure": 5000,
}

headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)

with urllib.request.urlopen(req) as res:
    print(res.status)