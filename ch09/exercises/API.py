import json
import requests

#Import 
#API Url

result =requests.get("https://v2.jokeapi.dev/joke/Any").json()


print(result)