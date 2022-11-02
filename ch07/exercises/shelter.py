import time
class Animal:
  def __init__(self,name,type):
    self.name=""
    self.type="dog"
    self.id=time.strftime("%d/%m/%y")
    self.arrive=time.strftime("%d/%m/%y")
    self.adopt
def main():
  b = Animal("dog")
  b.setAdopted()
main()