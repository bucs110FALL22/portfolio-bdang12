import requests

class HolidayAPI:
  def __init__(self,key='bf9a33f70b7e4707bb3a9206acdd5164'):
    self.url = f'https://holidays.abstractapi.com/v1/?api_key={key}&country=US&year=2020&month=12&day=25'
  def get(self):
    self.result = requests.get(self.url).json()
    print(self.result)

    