import requests

url_params = {'name': '賴珵武', 'score': 100}
r = requests.post('https://httpbin.org/post', data = url_params)
print(r.text)