import requests
request = 'http://127.0.0.1:5000/prime_number/31'
response = requests.get(request).json()
print(response)