import turtle
def drawEqShape(turtle,num_side, len_side):
  for i in range(num_side):
    bill.forward(len_side)
    bill.right(360/num_side)

bill=turtle.Turtle()
bill.shape("turtle")
bill.color("green")
num_side=int(input("Enter the num of sides"))
len_side=int(input("Enter the side lenght"))
drawEqShape(bill,num_side,len_side)
turtle.exitonclick()