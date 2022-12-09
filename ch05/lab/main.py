import pygame

# PART A

n = 101
count = 0

#(start n=101)

while n!=1:
  if n%2==0:
    n/=2
  else:
    n=(3*n)+1
  count+=1
  
print(n)
  
print("Count:", count)

#Part B

upper_limit = 20 
iters = {}  
num = 0  
attempt = 0  

# for loop

for start in range(2, upper_limit+1):
    num = 0  # reset count to 0 again
    attempt += 1
    value = start  # set the new starting value each time (ex: 2, 3, 4 ... 18, 19, 20)
    print("\nAttempt #{}:".format(attempt))
    while start != 1:
        print("\nStart #: {}".format(start))
        if (start % 2) == 0:
            num += 1
            print('Result: even')
            start /= 2
            print('Current: {}'.format(start))
        elif (start % 2) == 1:
            num += 1
            print('Result: odd')
            start = (start * 3) + 1
            print('Current: {}'.format(start))
    iters[value] = num

# store iters in a new variable as shown in instructions
iters_dict = iters


print("\n", iters_dict)

# Part C


pygame.init()

# create display
display = pygame.display.set_mode()


# variables
upper_limit = 20
iters = iters_dict
max_so_far = 0
max_val = 0
scale = 14
new = {}

# fill the screen with background color
display.fill('black')

# for loop for 3n+1 [2,20] (inclusive)
for n in range(2, upper_limit+1):
    pygame.display.flip()
    num = 0  # reset count to 0 again
    attempt += 1
    value = n  # set the new starting value each time (ex: 2, 3, 4 ... 18, 19, 20)
    # loop stops at n = 1 and statements inside check for even or odd #s
    while n != 1:
        if (n % 2) == 0:
            num += 1
            n /= 2
        elif (n % 2) == 1:
            num += 1
            n = (n * 3) + 1
    iters[value] = num
    # compare max_so_far with num, update max_val & max_so_far variables
    if max_so_far < num:
        max_val = value
        max_so_far = num
        print(f'Max Value: {max_val}\nMax So Far: {max_so_far}')

    # new dictionary puts compared values above in it
    new[max_val] = max_so_far
    # printing new dictionary
    print(new)

    # dictionary coordinates to listed tuples
    pairs = [(x * scale, y * scale) for (x, y) in iters.items()]

    # graph
    graph_display = pygame.Surface(display.get_size())
    pygame.draw.lines(graph_display, 'aqua', False, pairs)
    graph_display = pygame.transform.flip(graph_display, False, True)
    display.blit(graph_display, (0, 0))
    pygame.display.update()

   
    max_value_string = f'Max Value: {max_val}   Max So Far: {max_so_far}'

    # render string variable to display on screen
    font = pygame.font.Font(None, 18)
    msg = font.render(max_value_string, False, 'green')
    display.blit(msg, (0, 0))
    pygame.display.flip()
    pygame.time.wait(1000)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()