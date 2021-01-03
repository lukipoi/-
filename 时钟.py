import pygame,sys,datetime,math
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
PINK = (255,174,201)
ORANGE = (255,127,39)
RED = (255,0,0)
SIZE = (800,600)
POS = (400,300)
pygame.display.set_caption('时钟')
screen = pygame.display.set_mode(SIZE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)
    pygame.draw.circle(screen,BLACK,POS,200,2)
    pygame.draw.line(screen,RED,POS,(400,110),2)
    pygame.draw.line(screen,RED,POS,(400+math.sin(math.radians(6))*190,300-math.cos(math.radians(6))*190),2)
    pygame.display.flip()    
