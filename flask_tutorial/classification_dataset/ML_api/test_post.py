import requests

url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint
body = {
    "S1": 19.45,
    "S2": 26.9,
    "S3": 22.83,
    "S4": 30.1,
    "S5": 2.2,
    "S6": 13.4,
    "S7": 56.5
}
response = requests.post(url, data=body)
print (response.json())
