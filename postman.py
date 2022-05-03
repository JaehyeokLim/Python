from collections import requests

url = "203.253.128.161:7579/Mobius"

payload={}
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SOrigin'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
