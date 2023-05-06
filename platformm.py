import time,os

import matplotlib.pyplot as plt
import pygame
from platformm2 import value,character_png,timer\
    ,character,character_sprite
pygame.init()



class platfrom1:

    def __init__(self,width,height):
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption('RogueXFighter')
        self.tile = pygame.image.load(r"S:\platform\Rogue\tiles\tile.png")
        self.clock = pygame.time.Clock()



    def events(self):


        key = (pygame.key.get_pressed())


        if key[pygame.K_LEFT]:
            timer.stand_timer = time.time()
            value.stand = False
            value.last_key = "Left"
            character_sprite.x_moveing(self.window)


        elif key[pygame.K_RIGHT]:
            timer.stand_timer = time.time()
            value.stand = False
            value.last_key = "Right"
            character_sprite.x_moveing(self.window)


        elif key[pygame.K_UP] and (time.time()-timer.jump_timer)>0.1523235355344352345*2:
            timer.jump_timer = time.time()
            character_sprite.y_upping(self.window)
            value.stand = False

        elif key[pygame.K_DOWN]:
            value.y_move+=40

        else:

            if value.last_key=="Right" and value.last_key=="Left":
                if ((time.time()-timer.stand_timer>0.152523535534352345) and (time.time()-timer.stand_timer<0.152523535534352345*1.2)) :
                    value.stand = True

            else:
                if (time.time()-timer.jump_timer>0.1523235355344352345*2):
                    value.stand = True

                else:
                    character_sprite.y_upping(self.window)


    def mainloop(self):

        character_sprite.icon()
        character_sprite.background(self.window)
        character_sprite.stand(self.window)


        while True:
            pygame.time.delay(30)
            self.events()


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()







            character_sprite.stand(self.window)
            self.clock.tick(30)
            pygame.display.update()



platfrom1 = platfrom1(1200,720)

if __name__=='__main__':
    platfrom1.mainloop()