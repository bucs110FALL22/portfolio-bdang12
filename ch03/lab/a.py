import pygame
import math
pygame.init()
window = pygame.display.set_mode()



blue = [0,0,255]
white = [255,255,255]
window.fill(white)

coords = []
num_sides = 3
side_length = 75
offset = (100)


for i in range(num_sides):
 theta = (2.0 * math.pi * (i)) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append([x,y])
window.fill(white)
pygame.draw.polygon(window, blue, coords)

pygame.display.flip()

pygame.time.wait(500)
coords.clear()


num_sides = 4

for i in range(num_sides):
 theta = (2.0 * math.pi * (i)) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append([x,y])
window.fill(white)
pygame.draw.polygon(window, blue, coords)
pygame.display.flip()
pygame.time.wait(500)
coords.clear()


num_sides = 5

for i in range(num_sides):
 theta = (2.0 * math.pi * (i)) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append([x,y])
window.fill(white)
pygame.draw.polygon(window, blue, coords)
pygame.display.flip()
pygame.time.wait(500)
coords.clear()
num_sides = 9



for i in range(num_sides):
 theta = (2.0 * math.pi * (i)) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append([x,y])
window.fill(white)
pygame.draw.polygon(window, blue, coords)
pygame.display.flip()
pygame.time.wait(500)
coords.clear()


num_sides = 360

for i in range(num_sides):
 theta = (2.0 * math.pi * (i)) / num_sides
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 coords.append([x,y])
window.fill(white)
pygame.draw.polygon(window, blue, coords)
pygame.display.flip()
pygame.time.wait(500)
coords.clear()

#window.exitonclick()