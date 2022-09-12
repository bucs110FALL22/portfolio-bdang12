from turtle import *
color('purple')
shape('turtle')
n=int(input('Please enter the number of side:'))
l=int(input('Please enter the lenght of side:'))
color('purple')
shape('turtle')
pendown()
for x in range (n):
  forward(l)
  left(360/n)
penup()
done()
