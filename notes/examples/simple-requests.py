import requests

# GET
response = requests.get('https://ip.jsontest.com/')

print(f'Response object: {response}')
print(f'Response text: {response.text}')

# With payloads
payload = { 'q': 'chetan' }
response = requests.get('https://github.com/search', params=payload)
print(f'Request URL: {response.url}')

# POST
payload = { 'key1': 'value1' }
response = requests.get('https://httpbin.org/post', data=payload)
print(f'Response text: {response.json()}')

try:
    response = requests.get('https://httpbin.org/post', data=payload)
except requests.exceptions.RequestException as ex:
    print(f'Error response: {ex.message}')