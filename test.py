import requests

targe_url = "https://www.tiobe.com/tiobe-index/"

response = requests.get(targe_url)

print(response.text)