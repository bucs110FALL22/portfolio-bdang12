import pygame
import pygame.freetype
from random import choice, randint

RESOLUTION = 800, 600
FPS = 60
TILESIZE = 32
PLAYER_SPEED = 600
FALLING_SPEED = 400

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, falling_stuff, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill('dodgerblue')
        self.rect = self.image.get_rect(topleft=pos)
        self.falling_stuff = falling_stuff
        self.score = 0

    def update(self, dt, events):
        d = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]: d -= 1
        if pressed[pygame.K_d]: d += 1

        self.rect.move_ip(d * dt * PLAYER_SPEED, 0)
        display_rect = pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(display_rect)

        for stuff in pygame.sprite.spritecollide(self, self.falling_stuff, True):
            self.score += 1

class FallingStuff(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(choice(['red', 'yellow', 'green']))
        self.rect = self.image.get_rect(topleft=pos)
        
    def update(self, dt, events):
        self.rect.move_ip(0, FALLING_SPEED * dt)
        display_rect = pygame.display.get_surface().get_rect()
        if self.rect.top > display_rect.bottom:
            self.kill()

def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    dt, clock = 0, pygame.time.Clock()
    sprites = pygame.sprite.Group()
    falling_stuff = pygame.sprite.Group()
    player = Player((300, 500), falling_stuff, sprites)
    font = pygame.freetype.SysFont('Arial', 54)

    CREATE_STUFF = pygame.USEREVENT + 1
    pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == CREATE_STUFF:
                pygame.time.set_timer(CREATE_STUFF, randint(1000, 2000), True)
                FallingStuff((randint(50, 550), 32), falling_stuff, sprites)
        screen.fill('black')
        font.render_to(screen, (20, 20), f'Score: {player.score}', 'white')
        sprites.update(dt, events)
        sprites.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()