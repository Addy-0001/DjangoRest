import requests

endpoint = "http://127.0.0.1:8000/api/"

# -> Application Programming Interface HTTP Request
get_response = requests.get(endpoint, params={'abc': 123}, json={
                            "query": "Hello World"})

print(get_response.text)
print(get_response.status_code)

print(get_response.json())
# A normal HTTP Request will send back HTML as shown here.
# A REST API request which is also an HTTP request, will return JSON
# JSON is mostly what we will be working with.
