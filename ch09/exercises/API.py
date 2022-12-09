import requests
p='17.121.114.112'

r = requests.get(
    'https://applebot.seoapi.com/v1/validate/?ip=17.121.114.112'

).json()
print(r.get('valid', None))


# {
#     "ip": "17.000.000.001",
#     "timestamp": 1615471876.25665,
#     "valid": false
# }
# {
#     "ip": "17.121.114.112",
#     "timestamp": 1615471876.25665,
#     "valid": true
# }
