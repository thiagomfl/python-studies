import requests

url = 'https://thiagotec.com'
response = requests.get(url)

print(f'Your request to {url} came back {response.status_code}')

print(response.text)
