#Promblem 1
print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15)
#The number 0.66 runs indefinitely.
#Promblem 2
print('This is the money exchange system using the Euro to US Dollar.')
print('Be aware that we will charge $3.00 fees for using the service.')
rate=float(input('Please input the current exchange rate from the Euro to Dollar: '))
amount=float(input('Please input the amount of currency to exchange: '))
total=rate*amount
result=total-3.00
print('Your exchange is: $',result)