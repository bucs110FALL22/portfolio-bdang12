import pygame
pygame.init()
width = 700
height = 500
win = pygame.display.set_mode((width, height))
win.fill((0, 0, 0))

class button():
    def init(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def redrawWindow():
    win.fill((0, 0, 0))
    greenButton.draw(win, (0, 0, 0))
    redButton.draw(win, (0, 0, 0))
run = True
greenButton = button((0, 255, 0), 280, 190, 250, 100, "Start")
redButton = button((255, 0, 0), 280, 310, 250, 100, "Quit")
while run:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
                print("clicked the button")
            if redButton.isOver(pos):
                pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color = (105, 105, 105)
            else:
                greenButton.color = (0, 200, 0)
            if redButton.isOver(pos):
                redButton.color = (105, 105, 105)
            else:
                redButton.color = (255, 0, 0)