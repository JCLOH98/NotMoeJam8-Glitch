import math
import random
import time
import pygame
import sys
from pygame.locals import *

SCREENWIDTH = 720
SCREENHEIGHT = int(0.75*(SCREENWIDTH))

TVSCREENWIDTH = SCREENWIDTH + 100
TVSCREENHEIGHT = SCREENHEIGHT + 100

BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (180,180,180)
DARKGREY  =(100,100,100)
DARKERGREY = (50,50,50)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

PLAYERWIDTH = 80
PLAYERHEIGHT = 90
HITBOXWIDTH = 70
HITBOXHEIGHT = PLAYERHEIGHT

GLITCHWIDTH = PLAYERWIDTH
GLITCHHEIGHT = PLAYERHEIGHT/2
GLITCHTIME = 1 #seconds

ENEMYWIDTH = 60
ENEMYHEIGHT = 50
ENEMYSPEED = 5

LANE = 6 #1st lane is for display reason

FPS = 30

#pygame.display.set_icon(pygame.image.load(""))
pygame.init()

Display = pygame.display.set_mode((TVSCREENWIDTH, TVSCREENHEIGHT))
pygame.display.set_caption("Glitchman TV")

#pygame.mouse.set_cursor(*pygame.cursors.tri_left)

TheFont = pygame.font.Font("./font/ZCOOL_QingKe_HuangYou/ZCOOLQingKeHuangYou-Regular.ttf",30)

ENEMYGLITCH = pygame.transform.scale(pygame.image.load("./sprite/enemy_glitch.png"),(ENEMYWIDTH,ENEMYHEIGHT))
PLAYERGLITCH = pygame.transform.scale(pygame.image.load("./sprite/player_glitch.png"),(int(GLITCHWIDTH),int(GLITCHHEIGHT)))

WALK1 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk1new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK2 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk2new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK3 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk3new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK4 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk4new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK5 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk5new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK6 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk6new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK7 = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk7new.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))

WALK1BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk1new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK2BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk2new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK3BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk3new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK4BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk4new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK5BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk5new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK6BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk6new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))
WALK7BW = pygame.transform.scale(pygame.image.load("./sprite/player/Glitchman_Walk7new_bw.png").convert_alpha(),(PLAYERWIDTH,PLAYERHEIGHT))

PLAYERGLITCHBW = pygame.transform.scale(pygame.image.load("./sprite/player_glitch_bw.png"),(int(GLITCHWIDTH),int(GLITCHHEIGHT)))

RADIUS = 20
    
class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.playerrect = Rect(0,0,self.width,self.height)
        self.playerrect.center = (self.x,self.y)

class Enemy:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.enemyrect = Rect(0,0,width,height)
        self.enemylist = []

def startscreen():
    run = True
    while run:
        Display.fill(DARKERGREY)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    run = False
        pygame.draw.rect(Display, GREY, Rect((TVSCREENWIDTH - SCREENWIDTH)/2,(TVSCREENHEIGHT - SCREENHEIGHT)/2,SCREENWIDTH,SCREENHEIGHT))
        pygame.draw.rect(Display, WHITE, Rect((TVSCREENWIDTH - SCREENWIDTH)/2,(TVSCREENHEIGHT - SCREENHEIGHT)/2,SCREENWIDTH,SCREENHEIGHT),3)
        
        pygame.draw.circle(Display,DARKGREY,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS)

        pygame.draw.circle(Display,BLACK,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS,3)

        pygame.draw.circle(Display,DARKGREY,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*4),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS)

        pygame.draw.circle(Display,BLACK,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*4),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS,3)

        pygame.draw.circle(Display,DARKGREY,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*7),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS)

        pygame.draw.circle(Display,BLACK,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*7),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS,3)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        
    pass

def endscreen():
    pass

def main():
    run = True
    
    TheTime = 0
    Start = time.time()#start time

    #use to check the FPS
    frame = 0;
    realtimeFPS = 0
    previousFrame = 0

    #accurate timing
    frametiming = 0

    distance = 2*SCREENHEIGHT/LANE - 1*SCREENHEIGHT/LANE

    player = Player(PLAYERWIDTH/2 + (TVSCREENWIDTH - SCREENWIDTH)/2,(SCREENHEIGHT/LANE*3/2) + (TVSCREENHEIGHT - SCREENHEIGHT)/2,HITBOXWIDTH,HITBOXHEIGHT)
    enemy = Enemy(ENEMYWIDTH,ENEMYHEIGHT)

    glitch = False
    GlitchStart = 0
    glitchcount = 0

    spawnBoss = 0 #condition

    chance = 2
    collided = False

    playercount = 0
    
    while run:
        #for FPS
        End = time.time()#end time
        frame += 1
        frametiming += 1
        if (int(End) - int(Start) == 1):
                        TheTime += 1
                        Start = time.time()
                        #print(TheTime)
                        realtimeFPS = (frame - previousFrame)
                        #print("RealTimeFPS:", realtimeFPS,"\n")
                        previousFrame = frame 

                        

        #enemy spawn
        spawnBoss = random.randrange(0,5,1)
        if (frametiming % (FPS*2) == 0):
            if (spawnBoss == 1):
                enemyrect = Rect(0,0,ENEMYWIDTH,SCREENHEIGHT - SCREENHEIGHT/LANE)
                enemyrect.centerx = SCREENWIDTH - ENEMYWIDTH
                enemyrect.centery = SCREENHEIGHT/LANE * LANE/2 + SCREENHEIGHT/LANE/2 + (TVSCREENHEIGHT - SCREENHEIGHT)/2
                enemy.enemylist.append(enemyrect)
            else:
                randomlane = random.randrange((SCREENHEIGHT/LANE)*3/2, SCREENHEIGHT, distance)#the lane pixel
                enemyrect = Rect(0,0,ENEMYWIDTH,ENEMYHEIGHT)
                enemyrect.centerx = SCREENWIDTH - ENEMYWIDTH
                enemyrect.centery = randomlane + (TVSCREENHEIGHT - SCREENHEIGHT)/2
                enemy.enemylist.append(enemyrect)
            
                        
        Display.fill(DARKERGREY)

        #animation count for player
        playercount += 1

        if playercount == 7*(FPS/14):
            playercount = 0
        
        #Inputs
        key = pygame.key.get_pressed()

        if (key[K_k]):
            print("glitching")
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                  #print("up")
                  if (player.y != (SCREENHEIGHT/LANE)*3/2 + (TVSCREENHEIGHT - SCREENHEIGHT)/2):#2nd lane
                      player.y -= distance
                      player.playerrect.centery = player.y
                if event.key == K_s:
                    #print("down")
                    if (player.y != (SCREENHEIGHT) - (SCREENHEIGHT/LANE)/2 + (TVSCREENHEIGHT - SCREENHEIGHT)/2):#last lane
                        player.y += distance
                        player.playerrect.centery = player.y
                if event.key == K_j:
                    #print("glitch")
                    if glitch == False:
                        glitch = True


        #glitch logic
        if glitch == True:
            glitchcount += 1
            player.playerrect.height = GLITCHHEIGHT
            player.playerrect.width = GLITCHWIDTH
            player.playerrect.centery = player.y
            if glitchcount == int(0.75*FPS): #30 = 1 seconds
                glitchcount = 0
                glitch = False
            
        elif glitch == False:
             player.playerrect.height = HITBOXHEIGHT
             player.playerrect.width = HITBOXWIDTH
             player.playerrect.centery = player.y

        #enemy moving logic
        for i in range(len(enemy.enemylist)):
            enemy.enemylist[i].centerx -= ENEMYSPEED


        #collide logic
        for i in range(len(enemy.enemylist)):
            if (player.playerrect.colliderect(enemy.enemylist[i])) and player.playerrect.height == PLAYERHEIGHT and collided == False:
                chance -= 1
                collided = True

        if collided == True:
            if enemy.enemylist[0].right <= (TVSCREENWIDTH - SCREENWIDTH):
                collided = False

        
        #destroy enemy item
        for i in range(len(enemy.enemylist)):
            if enemy.enemylist[i].right <= (TVSCREENWIDTH - SCREENWIDTH):
                enemy.enemylist.remove(enemy.enemylist[i])
                break

        #game over logic
        if chance == 0:
            run = False
                    

        #draw
        pygame.draw.rect(Display, GREY, Rect((TVSCREENWIDTH - SCREENWIDTH)/2,(TVSCREENHEIGHT - SCREENHEIGHT)/2,SCREENWIDTH,SCREENHEIGHT))
        for i in range(LANE):
            pygame.draw.line(Display,WHITE,((TVSCREENWIDTH - SCREENWIDTH)/2, ((i+1)*(SCREENHEIGHT)/LANE) + (TVSCREENHEIGHT - SCREENHEIGHT)/2),(SCREENWIDTH + (TVSCREENWIDTH - SCREENWIDTH)/2, ((i+1)*(SCREENHEIGHT)/LANE) + (TVSCREENHEIGHT - SCREENHEIGHT)/2),3)
        pygame.draw.rect(Display, WHITE, Rect((TVSCREENWIDTH - SCREENWIDTH)/2,(TVSCREENHEIGHT - SCREENHEIGHT)/2,SCREENWIDTH,SCREENHEIGHT),3)
        
        pygame.draw.circle(Display,DARKGREY,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS)

        pygame.draw.circle(Display,BLACK,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS,3)

        pygame.draw.circle(Display,DARKGREY,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*4),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS)

        pygame.draw.circle(Display,BLACK,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*4),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS,3)

        pygame.draw.circle(Display,DARKGREY,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*7),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS)

        pygame.draw.circle(Display,BLACK,(int(TVSCREENWIDTH - math.ceil((TVSCREENWIDTH - SCREENWIDTH)/2) - RADIUS*7),
                                         int(TVSCREENHEIGHT - math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/2) + math.ceil((TVSCREENHEIGHT - SCREENHEIGHT)/4))),RADIUS,3)

        #pygame.draw.rect(Display,BLUE,player.playerrect,1)
        if chance == 2:
            if player.playerrect.height == PLAYERHEIGHT:
                if (playercount <= 1*(FPS/14)):
                    Display.blit(WALK1,player.playerrect)

                elif(playercount <= 2*(FPS/14)):
                    Display.blit(WALK2,player.playerrect)

                elif(playercount <= 3*(FPS/14)):
                    Display.blit(WALK3,player.playerrect)

                elif(playercount <= 4*(FPS/14)):
                    Display.blit(WALK4,player.playerrect)

                elif(playercount <= 5*(FPS/14)):
                    Display.blit(WALK5,player.playerrect)

                elif(playercount <= 6*(FPS/14)):
                    Display.blit(WALK6,player.playerrect)

                else:
                    Display.blit(WALK7,player.playerrect)
            else:
                Display.blit(PLAYERGLITCH, player.playerrect)

        elif chance == 1:
            if player.playerrect.height == PLAYERHEIGHT:
                if (playercount <= 1*(FPS/14)):
                    Display.blit(WALK1BW,player.playerrect)

                elif(playercount <= 2*(FPS/14)):
                    Display.blit(WALK2BW,player.playerrect)

                elif(playercount <= 3*(FPS/14)):
                    Display.blit(WALK3BW,player.playerrect)

                elif(playercount <= 4*(FPS/14)):
                    Display.blit(WALK4BW,player.playerrect)

                elif(playercount <= 5*(FPS/14)):
                    Display.blit(WALK5BW,player.playerrect)

                elif(playercount <= 6*(FPS/14)):
                    Display.blit(WALK6BW,player.playerrect)

                else:
                    Display.blit(WALK7BW,player.playerrect)
            else:
                Display.blit(PLAYERGLITCHBW, player.playerrect)

        

        for i in range(len(enemy.enemylist)):
            pygame.draw.rect(Display,RED,enemy.enemylist[i])
            if (enemy.enemylist[i].height == ENEMYHEIGHT):
                Display.blit(ENEMYGLITCH, enemy.enemylist[i])
            elif (enemy.enemylist[i].height != ENEMYHEIGHT):
                amount = int(math.ceil(enemy.enemylist[i].height / ENEMYHEIGHT))
                for j in range(amount):
                    Display.blit(ENEMYGLITCH, Rect(enemy.enemylist[i].left, enemy.enemylist[i].top + (j*ENEMYHEIGHT), enemy.enemylist[i].width, enemy.enemylist[i].height + (j*ENEMYHEIGHT)))

        Time = TheFont.render("Time: " + str(TheTime) + "s", True, BLACK)
        TimeRect = Time.get_rect()
        TimeRect.center = (TimeRect.width/2 + (TVSCREENWIDTH - SCREENWIDTH)/2 + 10, TimeRect.height/2 + (TVSCREENHEIGHT - SCREENHEIGHT)/2)
        Display.blit(Time,TimeRect)

        Chance = TheFont.render("Chance: " + str(chance), True, BLACK)
        ChanceRect = Chance.get_rect()
        ChanceRect.center = (ChanceRect.width/2 + (TVSCREENWIDTH - SCREENWIDTH)/2 + 10, TimeRect.height + ChanceRect.height/2 + (TVSCREENHEIGHT - SCREENHEIGHT)/2)
        Display.blit(Chance, ChanceRect)
        

        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        
startscreen()
main()
time.sleep(2)
pygame.quit()
sys.exit()

