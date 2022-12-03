
from random import choice
class Bomb:
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((32, 32))
        self.image.fill(choice(['red', 'yellow', 'green']))
        self.rect = self.image.get_rect(topleft=pos)
        
    def update(self, dt, events):
        self.rect.move_ip(0, 400 * dt)
        display_rect = pygame.display.get_surface().get_rect()
        if self.rect.top > display_rect.bottom:
            self.kill()
    
    
    
  
  