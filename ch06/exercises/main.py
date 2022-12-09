#Import modules
import pygame
from snake import *
from food import Food
from bomb import Bomb
import random
#Control Class
class Controller:
  def __init__(self):
    pygame.init()
    self.bounds = (300,300)
    #Set screen
    self.window = pygame.display.set_mode(self.bounds)
    pygame.display.set_caption("Shark")
    block_size = 20
    #input class models
    self.snake = Snake(block_size, self.bounds)
    self.food = Food(block_size,self.bounds)
    self.bomb = []
    self.bomb.append(Bomb(0, 0))
    
    #Mainnloop()
  def mainloop(self):
    font = pygame.font.SysFont('comicsans',60, True)
    self.run = True
    while self.run:
      pygame.time.delay(100)
      for bomb in self.bomb:
                bomb.update()
    #Program will stop when we stop the game
      
          
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
          #Control using button
      self.keys = pygame.key.get_pressed()
      if self.keys[pygame.K_LEFT]:
        self.snake.steer(Direction.LEFT)
      elif self.keys[pygame.K_RIGHT]:
        self.snake.steer(Direction.RIGHT)
      elif self.keys[pygame.K_UP]:
        self.snake.steer(Direction.UP)
      elif self.keys[pygame.K_DOWN]:
        self.snake.steer(Direction.DOWN)
        #This make shark automatically move foward
      self.snake.move()
      #THis make the shark eat the food and the food response in random pos
      self.snake.check_for_food(self.food)

      #If the shark in the screen edge: Game Over
      if self.snake.check_bounds() == True :
        self.text = font.render('Game Over', True, (255,255,255))
        self.window.blit(self.text, (20,120))
        pygame.display.update()
        pygame.time.delay(1000)
        self.snake.respawn()
        self.food.respawn()
      self.window.fill((255,0,0))
      #draw each  sprite
      self.snake.draw(pygame, self.window)
      self.food.draw(pygame, self.window)
      self.bomb.draw(pygame, self.window)
      #Show on screen
      pygame.display.update()
        
    
   
  
      
    
    
    
    
  #def drawshark(self):
    #shark=pygame.rect(self.pos.x*self)
  
def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()
    
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

