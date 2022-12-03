import pygame
from random import randint
from snake import *
from food import Food
from bomb import Bomb
class Controller:
  def __init__(self):
    pygame.init()
    self.bounds = (300,300)
    self.window = pygame.display.set_mode(self.bounds)
    pygame.display.set_caption("Snake")
    block_size = 20
    self.snake = Snake(block_size, self.bounds)
    self.food = Food(block_size,self.bounds)
    self.bomb = Bomb(block_size,self.bounds)
  def mainloop(self):
    font = pygame.font.SysFont('comicsans',60, True)
    self.run = True
    while self.run:
      pygame.time.delay(100)
    
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
      self.keys = pygame.key.get_pressed()
      if self.keys[pygame.K_LEFT]:
        self.snake.steer(Direction.LEFT)
      elif self.keys[pygame.K_RIGHT]:
        self.snake.steer(Direction.RIGHT)
      elif self.keys[pygame.K_UP]:
        self.snake.steer(Direction.UP)
      elif self.keys[pygame.K_DOWN]:
        self.snake.steer(Direction.DOWN)
      self.snake.move()
      self.snake.check_for_food(self.food)
      if self.snake.check_bounds() == True or self.snake.check_tail_collision() == True:
        self.text = font.render('Game Over', True, (255,255,255))
        self.window.blit(self.text, (20,120))
        pygame.display.update()
        pygame.time.delay(1000)
        self.snake.respawn()
        self.food.respawn()
      self.window.fill((0,0,0))
      self.snake.draw(pygame, self.window)
      self.food.draw(pygame, self.window)
      self.bomb.bomb(randint(50, 550), 32)
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

