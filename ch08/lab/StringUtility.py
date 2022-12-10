class StringUtility:
  def __init__(self, string):
    self.string = string

  # String Function
  def __str__(self):
    return self.string


def vowels(self):
    count = 0
    for i in self.string:
      if(i=="a" or i=="e"or i=="i" or i=="o" or i=="u"):
        count = count + 1
      if (count >5):
        return "many"
      else:
        return count

def bothEnds(self):
    size = len(self.string)
    if (size <= 2):
      return ""
    else:
      stng = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return stng

def fixStart(self):
    if len(self.string)>=1:
      firstchar= self.string[0]
      for i in self.string:
        self.star = self.string[1:].replace(firstchar,"*")
        return self.string[0]+ str
    else:
      return""

def asciiSum(self):
    str = 0
    for i in range(len(self.string)):
        str = str + ord(self.string[i])
    return str