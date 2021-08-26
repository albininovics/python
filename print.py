import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.text)
print(response.json())
result_json = response.json()
print(result_json['title'])


