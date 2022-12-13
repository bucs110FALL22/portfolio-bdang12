import CompanyAPI
import ApplebotAPI
def main():
    #Proxy Class
  result=CompanyAPI.CompanyAPI()
  result.get()
  result2=ApplebotAPI.ApplebotAPI()
  result2.get()
main()