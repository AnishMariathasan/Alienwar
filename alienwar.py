#! /usr/bin/env python
import pygame, sys
from pygame.locals import *

pygame.init()

LENGTH = 1278
HEIGHT = 660

ZONE = pygame.display.set_mode((LENGTH,HEIGHT))
pygame.display.set_caption('Game Zone')

import math , random

SF = 9

SPEED = random.randint(-20,20)/SF
SPEED2= random.randint(-20,20)/SF
SPEED3 = random.randint(-20,20)/SF
SPEED4 = random.randint(-20,20)/SF
SPEED5 = random.randint(-20,20)/SF
SPEED6 = random.randint(-20,20)/SF
SPEED7 = random.randint(-20,20)/SF
SPEED8 = random.randint(-20,20)/SF
SPEED9 = random.randint(-20,20)/SF
SPEED10 = random.randint(-20,20)/SF
SPEED11 = random.randint(-20,20)/SF




randx1 = random.randint(0,LENGTH)
randy1 = random.randint(0,HEIGHT)

randx2 = random.randint(0,LENGTH)
randy2 = random.randint(0,HEIGHT)

randx3 = random.randint(0,LENGTH)
randy3 = random.randint(0,HEIGHT)

randx4 = random.randint(0,LENGTH)
randy4 = random.randint(0,HEIGHT)

randx5 = random.randint(0,LENGTH)
randy5 = random.randint(0,HEIGHT)

randx6 = random.randint(0,LENGTH)
randy6 = random.randint(0,HEIGHT)

randx7 = random.randint(0,LENGTH)
randy7 = random.randint(0,HEIGHT)

randx8 = random.randint(0,LENGTH)
randy8 = random.randint(0,HEIGHT)

randx9 = random.randint(0,LENGTH)
randy9 = random.randint(0,HEIGHT)

randx10 = random.randint(0,LENGTH)
randy10 = random.randint(0,HEIGHT)

randx11 = random.randint(0,LENGTH)
randy11 = random.randint(0,HEIGHT)


BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
YELLOW=(255,255,0)
FUCHSIA=(255,0,255)
WHITE=(255,255,255)
LBLUE=(0,255,255)
BLACK=(0,0,0)
SAUCER=pygame.image.load('saucer.gif')
SAUCER2=pygame.image.load('ycraft.gif')
SAUCER3=pygame.image.load('ycraft.gif')
SAUCER4=pygame.image.load('saucer.gif')
SAUCER5=pygame.image.load('saucer.gif')
SAUCER6=pygame.image.load('saucer.gif')
SAUCER7=pygame.image.load('saucer.gif')
SAUCER8=pygame.image.load('saucer.gif')
SAUCER9=pygame.image.load('saucer.gif')
SAUCER10=pygame.image.load('saucer.gif')
SAUCER11=pygame.image.load('ycraft.gif')

SC1=pygame.image.load('sc1.gif')
SC2=pygame.image.load('sc2.gif')
SC3=pygame.image.load('sc3.gif')
SC4=pygame.image.load('sc4.gif')
SC5=pygame.image.load('sc5.gif')
SC6=pygame.image.load('sc6.gif')
SC7=pygame.image.load('sc7.gif')
SC8=pygame.image.load('sc8.gif')
SC9=pygame.image.load('sc9.gif')
SC10=pygame.image.load('sc10.gif')

MISSILE=pygame.image.load('missileR.gif')


SOUND=pygame.mixer.Sound('Pop.wav')
SOUND2=pygame.mixer.Sound('Explosion2.wav')
SOUND3=pygame.mixer.Sound('cannon.wav')
SOUND4=pygame.mixer.Sound('bomb.wav')
SOUND5=pygame.mixer.Sound('gun.wav')
SOUND6=pygame.mixer.Sound('jet.wav')
SOUND7=pygame.mixer.Sound('war.wav')
SOUND8=pygame.mixer.Sound('ufo.wav')
SOUND9=pygame.mixer.Sound('jet_doppler1.wav')

COUNTER = 0
EXITCOUNT = 0
SBCOUNT = 0
COLLISION = 0
SCOUNT = 300
JCOUNT = 500
MISSCOUNT = 1
MISSILEFIRE = 0
EXPLCOUNT2 = 0
EXPLCOUNT3 = 0
EXPLCOUNT4 = 0
EXPLCOUNT5 = 0
EXPLCOUNT6 = 0
EXPLCOUNT7 = 0
EXPLCOUNT8 = 0
EXPLCOUNT9 = 0
EXPLCOUNT10 = 0
EXPLCOUNT11 = 0

ALIVE2 = 2
ALIVE3 = 2
ALIVE4 = 2
ALIVE5 = 2
ALIVE6 = 2
ALIVE7 = 2
ALIVE8 = 2
ALIVE9 = 2
ALIVE10 = 2
ALIVE11 = 2

SATURNX = 600
SATURNY = 750

JUPITERX = 1500
JUPITERY = 200

S2x = randx2
S2y = randy2
S2dx = S2dy = SPEED2

S3x = randx3
S3y = randy3
S3dx = S3dy = SPEED3

S4x = randx4
S4y = randy4
S4dx = S4dy = SPEED4

S5x = randx5
S5y = randy5
S5dx = S5dy = SPEED5

S6x = randx6
S6y = randy6
S6dx = S6dy = SPEED6

S7x = randx7
S7y = randy7
S7dx = S7dy = SPEED7


S8x = randx8
S8y = randy8
S8dx = S8dy = SPEED8


S9x = randx9
S9y = randy9
S9dx = S9dy = SPEED9


S10x = randx10
S10y = randy10
S10dx = S10dy = SPEED10


S11x = randx11
S11y = randy11
S11dx = S11dy = SPEED11


w = ZONE.get_rect().width -10
h = ZONE.get_rect().height -10

x=y=10
mod_x=mod_y=10


clock=pygame.time.Clock()

while True :
        x+=mod_x
        y+=mod_y
        ZONE.fill(BLACK)
	
        SCOUNT = SCOUNT + 1	
	
        if SCOUNT <= 900: 	
                SATURNX = SCOUNT
                SATURNY = 450 - math.sqrt(90000 - (SATURNX - 600)*(SATURNX-600))
	
        if SCOUNT >900:
                SATURNX = 1800 - SCOUNT
                SATURNY = 450 + math.sqrt(90000 - (SATURNX - 600)*(SATURNX-600))
	
	

        if SCOUNT >= 1500: SCOUNT = 300
	



        BACKGROUND = pygame.image.load('sun.jpg')
        SUNCIRCLE=pygame.draw.circle(ZONE,BLACK,(625,483),48)
        ZONE.blit(BACKGROUND,(500,380))	

        BACKGROUND2 = pygame.image.load('jupiter 4.gif')
        JUPITER4CIRCLE=pygame.draw.circle(ZONE,BLACK,(1523,223),23)
        ZONE.blit(BACKGROUND2,(JUPITERX,JUPITERY))

        BACKGROUND3 = pygame.image.load('saturn2.jpg')

        ZONE.blit(BACKGROUND3,(SATURNX,SATURNY))
        

	
        SAUCERCIRCLE=pygame.draw.circle(ZONE,BLACK,(x+70,y+30),30)

	
	
	

	
	
        ZONE.blit(SAUCER,(x,y))
	
        if ALIVE2 > 1:
                SAUCERCIRCLE2=pygame.draw.circle(ZONE,BLACK,(S2x+60,S2y+50),30)
                ZONE.blit(SAUCER2,(S2x,S2y))
        if ALIVE3 > 1:
                SAUCERCIRCLE3=pygame.draw.circle(ZONE,BLACK,(S3x+60,S3y+50),30)
                ZONE.blit(SAUCER3,(S3x,S3y))
        if ALIVE4 > 1:
                SAUCERCIRCLE4=pygame.draw.circle(ZONE,BLACK,(S4x+60,S4y+50),30)
                ZONE.blit(SAUCER4,(S4x,S4y))
        if ALIVE5 > 1:
                SAUCERCIRCLE5=pygame.draw.circle(ZONE,BLACK,(S5x+60,S5y+50),30)
                ZONE.blit(SAUCER5,(S5x,S5y))
        if ALIVE6 > 1:
                SAUCERCIRCLE6=pygame.draw.circle(ZONE,BLACK,(S6x+60,S6y+50),30)
                ZONE.blit(SAUCER6,(S6x,S6y))
        if ALIVE7 > 1:
                SAUCERCIRCLE7=pygame.draw.circle(ZONE,BLACK,(S7x+60,S7y+50),30)
                ZONE.blit(SAUCER7,(S7x,S7y))
        if ALIVE8 > 1:
                SAUCERCIRCLE8=pygame.draw.circle(ZONE,BLACK,(S8x+60,S8y+50),30)
                ZONE.blit(SAUCER8,(S8x,S8y))
        if ALIVE9 > 1:
                SAUCERCIRCLE9=pygame.draw.circle(ZONE,BLACK,(S9x+60,S9y+50),30)
                ZONE.blit(SAUCER9,(S9x,S9y))
        if ALIVE10 > 1:
                SAUCERCIRCLE10=pygame.draw.circle(ZONE,BLACK,(S10x+60,S10y+50),30)
                ZONE.blit(SAUCER10,(S10x,S10y))
        if ALIVE11 > 1:
                SAUCERCIRCLE11=pygame.draw.circle(ZONE,BLACK,(S11x+60,S11y+50),30)
                ZONE.blit(SAUCER11,(S11x,S11y))	
        for event in pygame.event.get() :
                if event.type == QUIT :
                        pygame.quit()
                        sys.exit()
	
        if COLLISION == 1:
                SBCOUNT = SBCOUNT +1
                if 0 <= SBCOUNT < 4: 
                        SAUCER = SC1
                if 4 <= SBCOUNT < 8: 
                        SAUCER = SC2
                if 8 <= SBCOUNT < 12: 
                        SAUCER = SC3
                if 12 <= SBCOUNT < 16: 
                        SAUCER = SC4
                if 16 <= SBCOUNT < 20: 
                        SAUCER = SC5
                if 20 <= SBCOUNT < 24: 
                        SAUCER = SC6
                if 24 <= SBCOUNT < 28: 
                        SAUCER = SC7
                if 28 <= SBCOUNT < 32: 
                        SAUCER = SC8
                if 32 <= SBCOUNT < 36: 
                        SAUCER = SC9
                if 36 <= SBCOUNT < 40:
                        SAUCER = SC10
                if 40 <= SBCOUNT < 44: 
                        SAUCER = SC9
                if 44 <= SBCOUNT < 48: 
                        SAUCER = SC8
                if 48 <= SBCOUNT < 52: 
                        SAUCER = SC7
                if 52 <= SBCOUNT < 56: 
                        SAUCER = SC6
                if 56 <= SBCOUNT < 60: 
                        SAUCER = SC5
                if 60 <= SBCOUNT < 64: 
                        SAUCER = SC4
                if 64 <= SBCOUNT < 68: 
                        SAUCER = SC3
                if 68 <= SBCOUNT < 72: 
                        SAUCER = SC2
                if 72 <= SBCOUNT < 76: 
                        SAUCER = SC1
                if 76 <= SBCOUNT < 80: 
                        SAUCER = SC1
                if SBCOUNT > 80: 
                        SBCOUNT = 0
                        COLLISION = 0	







        keys=pygame.key.get_pressed()
        if keys[ pygame.K_RIGHT ] : mod_x = 10
        elif keys[ pygame.K_LEFT ] : mod_x = -10
        elif keys[ pygame.K_UP ] : mod_y = -10
        elif keys[ pygame.K_DOWN ] : mod_y = 10
        else : mod_x = mod_y = 0
	
        if x > LENGTH : x = LENGTH - 50
        if x < 0 : x = 50
        if y > LENGTH : y = LENGTH - 50
        if y < 0 : y = 50
        if y > HEIGHT : y = HEIGHT - 50
	
        if keys[ pygame.K_RETURN ] :
                MISSILEFIRE = 2
                MSX1 = MISSx
                MSY1 = MISSy
                SOUND9.play()

        if MISSILEFIRE < 1 :
                MISSx = x+10
                MISSy = y+40
	
        elif MISSILEFIRE > 1:
                MISSx = MSX1 + MISSCOUNT
                MISSy = MSY1
                MISSCOUNT = MISSCOUNT + 5

        MISSILECIRCLE=pygame.draw.circle(ZONE,LBLUE,(MISSx+80,MISSy+10),2)	
        ZONE.blit(MISSILE,(MISSx,MISSy))

        MISSDIST = math.sqrt((MISSx - x)*(MISSx - x) + (MISSy -y)*(MISSy - y))

        if (( S2x + S2dx ) > w ) or (( S2x + S2dx) < 10) : S2dx = -S2dx
        if (( S2y + S2dy ) > h ) or (( S2y + S2dy) < 10) : S2dy = -S2dy
        S2x += S2dx
        S2y += S2dy

        if (( S3x + S3dx ) > w ) or (( S3x + S3dx) < 10) : S3dx = -S3dx
        if (( S3y + S3dy ) > h ) or (( S3y + S3dy) < 10) : S3dy = -S3dy
        S3x += S3dx
        S3y += S3dy
	
	
        if (( S4x + S4dx ) > w ) or (( S4x + S4dx) < 10) : S4dx = -S4dx
        if (( S4y + S4dy ) > h ) or (( S4y + S4dy) < 10) : S4dy = -S4dy
        S4x += S4dx
        S4y += S4dy

        if (( S5x + S5dx ) > w ) or (( S5x + S5dx) < 10) : S5dx = -S5dx
        if (( S5y + S5dy ) > h ) or (( S5y + S5y) < 10) : S5dy = -S5dy
        S5x += S5dx
        S5y += S5dy


        if (( S6x + S6dx ) > w ) or (( S6x + S6dx) < 10) : S6dx = -S6dx
        if (( S6y + S6dy ) > h ) or (( S6y + S6dy) < 10) : S6dy = -S6dy
        S6x += S6dx
        S6y += S6dy


        if (( S7x + S7dx ) > w ) or (( S7x + S7dx) < 10) : S7dx = -S7dx
        if (( S7y + S7dy ) > h ) or (( S7y + S7dy) < 10) : S7dy = -S7dy
        S7x += S7dx
        S7y += S7dy


        if (( S8x + S8dx ) > w ) or (( S8x + S8dx) < 10) : S8dx = -S8dx
        if (( S8y + S8dy ) > h ) or (( S8y + S8dy) < 10) : S8dy = -S8dy
        S8x += S8dx
        S8y += S8dy

        if (( S9x + S9dx ) > w ) or (( S9x + S9dx) < 10) : S9dx = -S9dx
        if (( S9y + S9dy ) > h ) or (( S9y + S9dy) < 10) : S9dy = -S9dy
        S9x += S9dx
        S9y += S9dy


        if (( S10x + S10dx ) > w ) or (( S10x + S10dx) < 10) : S10dx = -S10dx
        if (( S10y + S10dy ) > h ) or (( S10y + S10dy) < 10) : S10dy = -S10dy
        S10x += S10dx
        S10y += S10dy


        if (( S11x + S11dx ) > w ) or (( S11x + S11dx) < 10) : S11dx = -S11dx
        if (( S11y + S11dy ) > h ) or (( S11y + S11dy) < 10) : S11dy = -S11dy
        S11x += S11dx
        S11y += S11dy


        if SUNCIRCLE.colliderect(SAUCERCIRCLE):
                SOUND3.play()
                S2dx = -SPEED2
                S2dy = -SPEED2
                COUNTER = COUNTER-10
                COLLISION = 1
                


        if JUPITER4CIRCLE.colliderect(SAUCERCIRCLE):
                SOUND5.play()
                S2dx = -SPEED2
                S2dy = -SPEED2
                COUNTER = COUNTER-10
                COLLISION = 1
		
        if SAUCERCIRCLE2.colliderect(SAUCERCIRCLE):
                SOUND3.play()
                S2dx = -SPEED2
                S2dy = -SPEED2
                COUNTER = COUNTER-10
                SAUCER2=pygame.image.load('ycraft2.gif')
                COLLISION = 1
		
		
        if SAUCERCIRCLE3.colliderect(SAUCERCIRCLE):
                SOUND3.play()
                S3dx = -SPEED3
                S3dy = -SPEED3
                COUNTER = COUNTER-10
                SAUCER3=pygame.image.load('ycraft2.gif')
                COLLISION = 1		

        if SAUCERCIRCLE4.colliderect(SAUCERCIRCLE):
                SOUND5.play()
                S4dx = -SPEED4
                S4dy = -SPEED4
                COUNTER = COUNTER-10
                SAUCER4=pygame.image.load('blastsaucer1.gif')
                COLLISION = 1
	
        if SAUCERCIRCLE5.colliderect(SAUCERCIRCLE):
                SOUND5.play()
                S5dx = -SPEED5
                S5dy = -SPEED5
                COUNTER = COUNTER-10
                SAUCER5=pygame.image.load('sauc2.gif')
                COLLISION = 1		

        if SAUCERCIRCLE6.colliderect(SAUCERCIRCLE):
                SOUND4.play()
                S6dx = -SPEED6
                S6dy = -SPEED6
                COUNTER = COUNTER-10
                SAUCER6=pygame.image.load('blastsaucer1.gif')
                COLLISION = 1

        if SAUCERCIRCLE7.colliderect(SAUCERCIRCLE):
                SOUND5.play()
                S7dx = -SPEED7
                S7dy = -SPEED7
                COUNTER = COUNTER-10	
                SAUCER7=pygame.image.load('blastsaucer1.gif')
                COLLISION = 1	
				
	
        if SAUCERCIRCLE8.colliderect(SAUCERCIRCLE):
                SOUND5.play()
                S8dx = -SPEED8
                S8dy = -SPEED8
                COUNTER = COUNTER-10	
                SAUCER8=pygame.image.load('blastsaucer1.gif')
                COLLISION = 1	

        if SAUCERCIRCLE9.colliderect(SAUCERCIRCLE):
                SOUND4.play()
                S9dx = -SPEED9
                S9dy = -SPEED9
                COUNTER = COUNTER-10	
                SAUCER9=pygame.image.load('blastsaucer1.gif')
                COLLISION = 1		

        if SAUCERCIRCLE10.colliderect(SAUCERCIRCLE):
                SOUND3.play()
                S10dx = -SPEED10
                S10dy = -SPEED10
                COUNTER = COUNTER-10		
                SAUCER10=pygame.image.load('blastsaucer1.gif')
                COLLISION = 1

        if SAUCERCIRCLE11.colliderect(SAUCERCIRCLE):
                SOUND4.play()
                S11dx = -SPEED11
                S11dy = -SPEED11
                COUNTER = COUNTER-10	
                SAUCER11=pygame.image.load('ycraft2.gif')
                COLLISION = 1

        if SAUCERCIRCLE2.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE2=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT2 = 1
        if EXPLCOUNT2 > 0:
                SAUCER2 = pygame.image.load('Explosion.gif')
                EXPLCOUNT2 = EXPLCOUNT2 + 1
                if EXPLCOUNT2 > 50:
                        ALIVE2 = 0

				

        if SAUCERCIRCLE3.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE3=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT3 = 1
        if EXPLCOUNT3 > 0:
                SAUCER3 = pygame.image.load('Explosion.gif')
                EXPLCOUNT3 = EXPLCOUNT3 + 1
                if EXPLCOUNT3 > 50:
                        ALIVE3 = 0
			
			

        if SAUCERCIRCLE4.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE4=pygame.draw.circle(ZONE,GREEN,(20000,1000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT4 = 1
        if EXPLCOUNT4 > 0:
                SAUCER4 = pygame.image.load('Explosion.gif')
                EXPLCOUNT4 = EXPLCOUNT4 + 1
                if EXPLCOUNT4 > 50:
                        ALIVE4 = 0


        if SAUCERCIRCLE5.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE5=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT5 = 1
        if EXPLCOUNT5 > 0:
                SAUCER5 = pygame.image.load('Explosion.gif')
                EXPLCOUNT5 = EXPLCOUNT5 + 1
                if EXPLCOUNT5 > 50:
                        ALIVE5 = 0


        if SAUCERCIRCLE6.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE6=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT6 = 1
        if EXPLCOUNT6 > 0:
                SAUCER6 = pygame.image.load('Explosion.gif')
                EXPLCOUNT6 = EXPLCOUNT6 + 1
                if EXPLCOUNT6 > 50:
                        ALIVE6 = 0

	
        if SAUCERCIRCLE7.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE7=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT7 = 1
        if EXPLCOUNT7 > 0:
                SAUCER7 = pygame.image.load('Explosion.gif')
                EXPLCOUNT7 = EXPLCOUNT7 + 1
                if EXPLCOUNT7 > 50:
                        ALIVE7 = 0

	
        if SAUCERCIRCLE8.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE8=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT8 = 1
        if EXPLCOUNT8 > 0:
                SAUCER8 = pygame.image.load('Explosion.gif')
                EXPLCOUNT8 = EXPLCOUNT8 + 1
                if EXPLCOUNT8 > 50:
                        ALIVE8 = 0

	

        if SAUCERCIRCLE9.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE9=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT9 = 1
        if EXPLCOUNT9 > 0:
                SAUCER9 = pygame.image.load('Explosion.gif')
                EXPLCOUNT9 = EXPLCOUNT9 + 9
                if EXPLCOUNT9 > 50:
                        ALIVE9 = 0

        if SAUCERCIRCLE10.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE10=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT10 = 1
        if EXPLCOUNT10 > 0:
                SAUCER10 = pygame.image.load('Explosion.gif')
                EXPLCOUNT10 = EXPLCOUNT10 + 1
                if EXPLCOUNT10 > 50:
                        ALIVE10 = 0


        if SAUCERCIRCLE11.colliderect(MISSILECIRCLE):
                if MISSDIST > 100: 
                        COUNTER = COUNTER + 100
                        SOUND2.play()
                        SAUCERCIRCLE11=pygame.draw.circle(ZONE,GREEN,(20000,10000),30)
                        MISSILEFIRE = 0
                        MISSCOUNT = 1
                        EXPLCOUNT11 = 1
        if EXPLCOUNT11 > 0:
                SAUCER11 = pygame.image.load('Explosion.gif')
                EXPLCOUNT11 = EXPLCOUNT11 + 1
                if EXPLCOUNT11 > 50:
                        ALIVE11 = 0
                        
        if MISSx > 1850 :
                MISSILEFIRE = 0
                MISSCOUNT = 1
        FONT = pygame.font.Font( 'freesansbold.ttf' , 30)
        TEXT = FONT.render( str(COUNTER), True, RED, BLACK)
        TEXT2 = FONT.render( 'bad luck', True, GREEN, RED)
        TEXT3 = FONT.render( 'WELL DONE', True, GREEN, RED)
        ZONE.blit(TEXT, (100,600) ) 
	
        if COUNTER > 20000:
                ZONE.blit(TEXT3, (80,450) )
                EXITCOUNT = EXITCOUNT + 1
                if EXITCOUNT > 40000:

                        pygame.quit()
                        sys.exit()
        pygame.display.update()
        clock.tick(300)

	
