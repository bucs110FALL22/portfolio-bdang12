import random
random_no=random.randint(1,10)
for i in range (3):
  guess_no=int(input("please enter the guess number: "))
  i++1
  if guess_no>random_no:
    print("The guess number is to large")
  elif guess_no<random_no:
    print("The guess number is to small")
  else:
    print("Correct!!!")
    break
if i==2:
  print("You fail!!!")