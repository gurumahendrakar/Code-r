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


        if (value.jump): # upping content are here

            if (time.time() - timer.jump_timer) < (0.6000000000000/1.5) and not (value.value_stand):
                value.upping = True
                value.downing = True
                character_sprite.y_upping(self.window)



            else:
                #value.upping  & value.dowing anyone flase do not work mein ___Right __ event


                if value.upping==True: #
                    value.jumpR_timer = time.time()
                    value.upping = False


                if (value.y_move!=600):

                    # full down content are here don't confuse

                    if (time.time()-value.jumpR_timer)>0.15353256235353534341*1.6:
                        value.do_not = False


                    if (time.time()-timer.runnT)<0.225352525355353 and value.do_not: # jump karne ke baad kitna right jaana hai

                        character_sprite.background(self.window)

                        if (value.last_key=="Left"):

                            value.x_move-=40
                            image = character_png.ljump_sprite[value.y_move_value]
                            platform.blit(pygame.image.load(image), (value.x_move - 90, value.y_move - 30))

                        else:

                            value.x_move += 40
                            image = character_png.rjump_sprite[value.y_move_value]
                            platform.blit(pygame.image.load(image), (value.x_move - 60, value.y_move - 30))


                        value.afterdown_rightClicked+=1



                    else:
                        character_sprite.standChecking()
                        

                        if value.value_stand:

                            if (time.time()-timer.runnT>0.21353435343434434/2):
                                character_sprite.stand(self.window)


                            else:
                                character_sprite.x_moveing(self.window)


                            if (time.time()-timer.jump_timer)<(0.6000000000000/1.5):
                                character_sprite.y_upping(self.window)
                                value.standJumpCount += 1





                        else:
                            # jab kaha pe stand nahi karega ye chalega
                            value.y_move+=60
                            character_sprite.y_downing(self.window)


                else:
                    value.upping = False
                    value.downing = False
                    value.jump = False
                    value.do_not = True
                    value.afterdown_rightClicked = 0
                    character_sprite.stand(self.window)



    def main_content(self):



        pygame.time.delay(10)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if ((event.key == pygame.K_LEFT) and value.afterdown_rightClicked<3) \
                        or (event.key==pygame.K_LEFT and value.value_stand):

                    value.last_key = "Left"
                    timer.runnT = time.time()

                    if not (value.downing) :
                        character_sprite.x_moveing(self.window)


                elif ((event.key == pygame.K_RIGHT) and value.afterdown_rightClicked<3)\
                        or (event.key==pygame.K_RIGHT) and value.value_stand:


                    value.last_key = "Right"
                    timer.runnT = time.time()

                    if not (value.upping)  and not (value.downing):
                        character_sprite.x_moveing(self.window)


                elif not (value.jump) or value.value_stand:
                    timer.jump_timer = time.time()

                    if (event.key == pygame.K_UP) and not value.value_stand:
                        timer.jump_timer = time.time()
                        value.jump = True



                elif (event.key == pygame.K_DOWN):
                    value.y_move += 100





        platfrom1.AfterRunStand()

        for x in range(20):
            self.window.blit(pygame.image.load(r'S:\platform\Rogue\ground.png'),(60*x,680))



        for x in range(7):
            self.window.blit(pygame.image.load(r"C:\Users\mahen\Downloads\craftpix-781131-free-swamp-game-tileset-pixel-art\1 Tiles\Tile_52.png"),(200+30*x,500))

        self.window.blit(pygame.image.load(
            r"C:\Users\mahen\Downloads\craftpix-781131-free-swamp-game-tileset-pixel-art\1 Tiles\Tile_52.png"),
                         (500, 440))




        pygame.time.Clock().tick(30)
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