a=int(input("Enter number of rows"))
for i in range(a):
    print("*"*(i+1))
for j in range(a):
    print("*"*(a-j))
    
#Second solutions
def star_pyramid():
  levels = int(input("Enter the desired pyramid height: "))
    
  for i in range(1, levels + 1):
    print("*" * i)

#define a function
def rstar_pyramid():
  levels = int(input("Enter the desired pyramid height: "))
  for i in range(levels, 0, -1):
    print("*" * i)
levels = int(input("Enter the desired pyramid height: "))
print(levels, id(levels))
levels = int(input("Enter the desired pyramid height: "))
print(levels)
star_pyramid(levels)
rstar_pyramid(levels)

  