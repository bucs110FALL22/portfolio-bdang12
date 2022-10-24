#Question1
def multiply(num):
  result = 0
  for i in range(num):
    result = result + num
  return result


#Question2
def exponent(num,exp):
  result=1
  for i in range(exp):
    result=result * num
  return result

  
#Question3
def square(num):
  return multiply(num)
  #return exponent(num,2)

def main():
  res = multiply(0)
  print(res)
  res = multiply(10)
  print(res)
  res=exponent(2,5)
  print(res)
  res=square(2)
  print(res)
main()