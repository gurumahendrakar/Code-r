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


    def AfterRunStand(self):
       if (time.time()-timer.runnT)>0.21353435343434434 and not (value.jump):
           character_sprite.stand(self.window)


  



    def jump(self,platform):

        if (value.jump):
            if (time.time() - timer.jump_timer) < 0.6000000000000/2:
                value.downing = True
                character_sprite.y_moveing(self.window)


            else:

                value.downing = False
                if (value.y_move!=560):


                    value.y_move+=80
                    character_sprite.y_downing(self.window)

                else:
                    character_sprite.stand(self.window)
                    value.jump = False



    def main_content(self):
        pygame.time.delay(70)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if (event.key == pygame.K_LEFT):

                    value.last_key = "Left"
                    timer.runnT = time.time()
                    character_sprite.x_moveing(self.window)


                elif (event.key == pygame.K_RIGHT):

                    value.last_key = "Right"

                    if not (value.downing):
                        timer.runnT = time.time()
                        character_sprite.x_moveing(self.window)


                elif (event.key == pygame.K_UP):

                    value.jump = True
                    timer.jump_timer = time.time()


                elif (event.key == pygame.K_DOWN):

                    value.y_move += 100

    def mainloop(self):
        character_sprite.icon()
        character_sprite.background(self.window)


        while True:

            platfrom1.main_content()

            if (value.jump):
                platfrom1.jump(self.window)


            platfrom1.AfterRunStand()
            pygame.time.Clock().tick(30)
            pygame.display.flip()


platfrom1 = platfrom1(1200,640)

if __name__=='__main__':
    platfrom1.mainloop()