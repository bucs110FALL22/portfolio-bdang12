
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = cost_per_week/classes_per_week
print("Cost per class:", cost_per_class)
#Prints both the value and the type of the variable
print("weeks", type(weeks))
print("classes", type(classes))
print("tuition", type(tuition))
print("cost_per_week", type(cost_per_week))
print("classes_per_week", type(classes_per_week))
print("cost_per_class", type(cost_per_class))


#Part B
import random
list = [1,2,3,4,5]
rand = random.choice(list)
print(rand)

#Part C
