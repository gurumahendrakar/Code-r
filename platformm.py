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


        self.jump_timer = 0
        self.afterdown_rightClicked = 0

        self.jumpR_timer = 0


    def AfterRunStand(self):
       if (time.time()-timer.runnT)>0.21353435343434434 and not (value.jump):

           character_sprite.stand(self.window)


  



    def jump(self,platform):

        if (value.jump):
            if (time.time() - timer.jump_timer) < (0.6000000000000/1.5):

                value.upping = True
                value.downing = True
                character_sprite.y_moveing(self.window)


            else:
                if value.upping==True:
                    self.jumpR_timer = time.time()
                    value.upping = False

                if (value.y_move!=600):


                    if (time.time()-timer.runnT)<0.125352525355353:

                        character_sprite.background(self.window)

                        if (value.last_key=="Left"):
                            value.x_move-=30
                            image = character_png.ljump_sprite[value.y_move_value]
                            platform.blit(pygame.image.load(image), (value.x_move - 90, value.y_move - 30))

                        else:
                            value.x_move += 30
                            image = character_png.rjump_sprite[value.y_move_value]
                            platform.blit(pygame.image.load(image), (value.x_move - 60, value.y_move - 30))


                        self.afterdown_rightClicked+=1



                    else:
                        print(self.afterdown_rightClicked)
                        value.y_move+=60
                        character_sprite.y_downing(self.window)

                else:

                    value.downing = False
                    self.jump_timer = 0
                    character_sprite.stand(self.window)
                    value.jump = False
                    self.afterdown_rightClicked = 0



    def main_content(self):

        pygame.time.delay(30)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if (event.key == pygame.K_LEFT) and self.afterdown_rightClicked<3:


                    value.last_key = "Left"
                    timer.runnT = time.time()

                    if not (value.downing) :
                        character_sprite.x_moveing(self.window)


                elif (event.key == pygame.K_RIGHT) and self.afterdown_rightClicked<3:


                    value.last_key = "Right"
                    timer.runnT = time.time()

                    if not (value.upping)  and not (value.downing):
                        character_sprite.x_moveing(self.window)


                elif not (value.jump):

                    if (event.key == pygame.K_UP):

                        if (self.afterdown_rightClicked==0):
                            value.jump = True
                            timer.jump_timer = time.time()


                elif (event.key == pygame.K_DOWN):

                    value.y_move += 100



        platfrom1.AfterRunStand()
        pygame.time.Clock().tick(90)
        pygame.display.flip()

    def mainloop(self):
        character_sprite.icon()
        character_sprite.background(self.window)


        while True:

            platfrom1.main_content()

            if (value.jump):
                platfrom1.jump(self.window)





platfrom1 = platfrom1(1200,720)

if __name__=='__main__':
    platfrom1.mainloop()