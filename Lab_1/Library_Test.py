import requests

r = requests.get('https://google.com')
print("Статус-код відповіді:", r.status_code)
