import HolidayAPI
import ApplebotAPI
def main():
    #Proxy Class
  result=HolidayAPI.HolidayAPI()
  result.get()
  result2=ApplebotAPI.ApplebotAPI()
  result2.get()
main()