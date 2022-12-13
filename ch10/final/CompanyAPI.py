import requests

class CompanyAPI:
  def __init__(self):
    self.url = '  https://companyenrichment.abstractapi.com/v1/?api_key=a1381d169c6245fba613ac609107eeac&domain=airbnb.com'
  def get(self):
    self.result = requests.get(self.url).json()
    for key,value in self.result.items():
      print(key,':',value)
  