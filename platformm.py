import time,os

import matplotlib.pyplot as plt
import pygame
from platformm2 import value,sprite,run,timer\
    ,character,character_sprite,attack
pygame.init()



class platfrom1:

    def __init__(self,width,height):
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption('RogueXFighter')
        self.tile = pygame.image.load(r"S:\platform\Rogue\tiles\tile.png")


    def sprite_timeing(self):

        stand_or_not = character_sprite.tile1_StandChecking()

        if  (stand_or_not):
            value.upClicked = True


        if value.attack_finished==True:
            if (time.time()-timer.attack_timer)>0.180343434343434:
                value.attack_finished = False


        if (time.time() - timer.runnT) > 0.1803434343434 and value.jump==False and not value.attack_finished:
            character_sprite.stand(self.window)




    def mainloop(self):
        character_sprite.icon()
        character_sprite.background(self.window)
        character_sprite.stand(self.window)



        while True:
            pygame.time.delay(70)

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    pygame.quit()


                if event.type==pygame.KEYDOWN:

                    if (event.key==pygame.K_LEFT):

                        value.last_key = "Left"
                        value.jump_right = "Left"

                        timer.jump_right_timer = time.time()


                        if (value.jump_finished and value.upClicked) or (
                                value.last_key == 'Left' and value.down == False):
                            timer.runnT = time.time()
                            value.x_move -= 20

                            character_sprite.tile1_StandChecking()
                            character_sprite.x_moveing(self.window)



                    elif (event.key==pygame.K_RIGHT):
                        value.last_key = "Right"
                        value.jump_right = "Right"
                        timer.jump_right_timer = time.time()


                        if (value.jump_finished and value.upClicked) or (value.last_key=='Right' and value.down==False):
                            timer.runnT = time.time()
                            character_sprite.x_moveing(self.window)
                            value.x_move+=20





                    elif (event.key==pygame.K_UP):
                        if not (value.down):
                            value.upClicked = 'UP'
                            timer.jump_timer = time.time()
                            timer.up_timer = time.time()
                            value.jump = True



                    elif (event.unicode=='a'):
                        value.attack_finished = True
                        timer.attack_timer = time.time()
                        character_sprite.attack(self.window)




            # full up down panel handleing brother
            if (value.upClicked): # ye isliye liya hai ki loop continue na chale

                if (value.jump) and (time.time()-timer.jump_timer)<0.2083053435343*2:
                    value.down = True # up button click na ho jab updar jaa raha ho

                    if (value.jump_right=='Right'):
                        if (time.time()-timer.jump_right_timer)<0.93853435343434:
                            value.x_move+=30
                        else:
                            value.jump_right = False


                    elif value.jump_right=='Left':

                        if (time.time()-timer.jump_right_timer)<0.93853435343434:
                            value.x_move-=30
                        else:
                            value.jump_right = False


                    if not(character_sprite.tile1_UpChecking()):
                            value.y_move-=50

                    character_sprite.jump_down_moveing(self.window)


                else:
                    value.jump_finished = True
                    value.down = True
                    character_sprite.tile1_StandChecking()

                    if value.y_move!=800 and not(value.standed):


                        value.y_move+=50

                        if (time.time()-timer.attack_timer)<0.135343534335343434:
                            character_sprite.attack(self.window)

                        else:
                            character_sprite.jump_down_moveing(self.window)



                    elif (value.y_move==800):
                        value.jump_finished = False
                        value.down = False

                        if (time.time()-timer.runnT)> 0.1803434343434:
                            character_sprite.stand(self.window)
                            value.upClicked = False
                            value.jump = False





            plat.sprite_timeing()
            self.window.blit(self.tile,(300,485))
            self.window.blit(self.tile,(700,485))
            pygame.time.Clock().tick(30)
            pygame.display.flip()


plat = platfrom1(1200,900)

if __name__=='__main__':
    plat.mainloop()