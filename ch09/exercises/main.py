import requests
url='https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=4658&manga=4199&manga=11608'
result = requests.get(url)
print(*result.content)