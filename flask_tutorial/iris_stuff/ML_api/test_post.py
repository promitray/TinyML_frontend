import requests

url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint
body = {
    "petal_length": 10,
    "sepal_length": 10,
    "petal_width": 10,
    "sepal_width": 10
}
response = requests.post(url, data=body)
print (response.json())
