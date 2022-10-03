import turtle
import random
window = turtle.Screen()
window.size(100,100)
window.bgcolor('lightblue')
Turtle = turtle.Turtle()
Turtle.shape('turtle')
Turtle.color('orange')
Turtle.up()
Turtle.goto(0,0)
while True:
  i=random.randint(1,2)
  if i==1:
    print("heads")
    Turtle.left(90)
    Turtle.forward(50)
  else:
    print("tail")
    Turtle.right(90)
    Turtle.forward(50)
