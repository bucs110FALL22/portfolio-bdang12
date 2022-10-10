import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() #cd  3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange(1,100)
y = random.randrange(1,100)
michelangelo.forward(x)
leonardo.forward(y)
michelangelo.goto(-100,-20)
leonardo.goto(-100,20)
n=0
while n<10:
  z = random.randrange(1,100)
  t = random.randrange(1,100)
  michelangelo.forward(z)
  leonardo.forward(t)
  n+=1
michelangelo.goto(-100,-20)
leonardo.goto(-100,20)
# PART B - complete part B here


window.exitonclick()
