import requests

class ApplebotAPI:
  def __init__(self, ip1='17.121.114.112', ip2='17.000.000.000'):
    self.url_1 = f'https://applebot.seoapi.com/v1/validate/?ip={ip1}'
    self.url_2 = f'https://applebot.seoapi.com/v1/validate/?ip={ip2}'
  def get(self):
    self.result = requests.get(self.url_1).json()
    self.show = requests.get(self.url_2).json()
    print(self.result.get('ip'))
    print(self.result.get('valid'))
    print(self.show.get('ip'))
    print(self.show.get('valid'))
    