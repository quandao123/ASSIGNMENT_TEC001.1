import requests
request = 'http://127.0.0.1:5000/airport/LFLL'
response = requests.get(request).json()
print(response)