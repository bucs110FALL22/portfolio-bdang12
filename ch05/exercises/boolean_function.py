def percentage_to_letter(score=0):
  if score >=90:
    letter='A' 
  elif score >=80 and score < 90:
    letter='B' 
  elif score >=70 and score < 80:
    letter='C' 
  elif score >=60 and score < 70:
    letter='D' 
  else:
    letter='F'
  return letter
def is_passing(letter=None):
  if letter=='A' or letter=='B' or letter=='C':
    return True
  else:
    return False
score=float(input('Enter the score:'))
var = percentage_to_letter(score)
var2 = is_passing(var)
print(var2)

