import pygame
import math
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (30, 134, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255,140,0)
YELLOW = (255,215,0)
PURPLE = (148,0,211)

class CirclePair:
    theta = 180.0
    def __init__(self,c,x,y,stepDiv):
        self.c = c
        self.x = x
        self.y = y
        self.stepDiv = stepDiv
        self.topX = x - 30
        self.topY = y
        self.sideX = self.topX-(x-y)
        self.sideY = self.topY+50+(100*((x-100)/100))

    def drawRing(self):
        pygame.draw.circle(screen,self.c,(self.x,self.y),35)
        pygame.draw.circle(screen,self.c,(self.y,self.x),35)
        pygame.draw.circle(screen,BLACK,(self.x,self.y),25)
        pygame.draw.circle(screen,BLACK,(self.y,self.x),25)

    def drawTrack(self):
        pygame.draw.circle(screen,WHITE,(int(self.topX),int(self.topY)),5)
        pygame.draw.circle(screen,WHITE,(int(self.sideX),int(self.sideY)),5)
        
    def update(self):
        if(step % self.stepDiv == 0):
            if(self.theta < 360.0):
                self.theta+=1
                self.topX = 30 * math.cos(math.radians(self.theta)) + self.x
                self.topY = 30 * math.sin(math.radians(self.theta)) + self.y
                self.sideX = self.topX-(self.x-self.y)
                self.sideY = self.topY+50+(100*((self.x-100)/100))
            else:
                self.theta = 0

def addColor(a,b):
    red = int(math.sqrt(0.5 * math.pow(a[0],2) + 0.5 * math.pow(b[0],2)));
    green = int(math.sqrt(0.5 * math.pow(a[1],2) + 0.5 * math.pow(b[1],2)));
    blue = int(math.sqrt(0.5 * math.pow(a[2],2) + 0.5 * math.pow(b[2],2)));
    return (red,green,blue);


list = []
list.append(CirclePair(RED,135,50,5))
list.append(CirclePair(ORANGE,235,50,4))
list.append(CirclePair(YELLOW,335,50,3))
list.append(CirclePair(GREEN,435,50,2))
list.append(CirclePair(BLUE,535,50,1))
step = 1
count = 0

size = (700,700)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
background = pygame.Surface((700,700))
background.convert()

while not done:
    screen.blit(background,(0,0))
    
    for o in list:
        o.drawRing()
        o.drawTrack()
    for o in list:
        o.update()
    for o in list:
        for u in list:
            pygame.draw.line(screen,WHITE,(o.topX,o.topY),(o.topX,u.sideY))
            pygame.draw.line(screen,WHITE,(o.sideX,o.sideY),(u.topX,o.sideY))
            background.set_at((int(o.topX), int(u.sideY)), addColor(o.c,u.c))
            count+=1
    step+=1
    pygame.display.update()
    clock.tick(120)
    for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   done = True
pygame.display.quit()
pygame.quit()

