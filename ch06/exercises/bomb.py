import pygame
import random
class Bomb:
    block_size = None
    color = (0,0,0)
  #Set the bomb location
    #x = 150; 
    #y = 0; 

    def __init__(self, x, y):
      self.image = pygame.Surface((200, 350))
      self.rect=self.image.get_rect()
      self.direction= "UP"        
      self.rect.x = x
      self.rect.y = y
#Draw a bomb
    def draw(self, game, window):
        game.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.block_size, self.block_size))
    def update(self):
      self.rect.y = self.rect.y - 1
      self.rect.x=random.randrange(-1, 2)