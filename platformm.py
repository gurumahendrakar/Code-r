import time,os

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

        if ((key[pygame.K_LEFT]) and (time.time()-timer.jump_timer) >0.152323535534435234452*1.2) and (value.jump_runCount<6 and value.jump_limit):

            if not (value.value_600):
                value.jump_runCount+=1


            timer.jump_run = time.time()
            timer.stand_timer = time.time()
            value.stand = False
            value.last_key = "Left"

            if (value.value_600==False) and (value.y_move<=420):
                value.x_move-=20
                character_sprite.background(self.window)

                self.window.blit(character_png.ljump_runn_sprite, (value.x_move - 90, value.y_move - 30))

            else:
                value.jump_limit = False

            if value.value_600:
                character_sprite.x_moveing(self.window)



        elif ((key[pygame.K_RIGHT]) and (time.time()-timer.jump_timer)>0.152323535534435234452*1.2) and ((value.jump_runCount<6 and value.jump_limit)):
            print("Right Clicked !!")
            if not value.value_600:
                value.jump_runCount+=1

            timer.jump_run = time.time()
            timer.stand_timer = time.time()
            value.stand = False
            value.last_key = "Right"


            if (value.value_600 == False) and (value.y_move<=420):

                value.x_move+=20
                character_sprite.background(self.window)
                self.window.blit(character_png.rjump_runn_sprite, (value.x_move - 90, value.y_move - 30))

            else:
                value.jump_limit = False


            if value.value_600:
                character_sprite.x_moveing(self.window)


        elif key[pygame.K_UP] and value.value_600:

            timer.jump_timer = time.time()
            character_sprite.y_upping(self.window)
            value.stand = False
            value.jump_limit = True
            value.value_600 = False


        elif key[pygame.K_DOWN]:
            value.y_move+=60


        else:

            if (time.time()-timer.jump_timer)<0.152323535534435234452*1:
                character_sprite.y_upping(self.window)


            elif value.y_move!=600 and (time.time()-timer.jump_timer)>0.15232353553443523445*1:

                if timer.jump_run == False:
                    timer.jump_run = time.time()

                value.y_move+=60
                character_sprite.y_downing(self.window)

            else:
                value.stand = True
                value.value_600  = True
                value.jump_runCount = 0
                timer.jump_run = 0


            if value.last_key=="Right" or value.last_key=="Left" and value.y_move==600:
                if ((time.time()-timer.stand_timer>0.152523535534352345) and (time.time()-timer.stand_timer<0.152523535534352345*1.2)) :
                    value.stand = True


    def mainloop(self):

        character_sprite.icon()
        character_sprite.background(self.window)
        character_sprite.stand(self.window)





        while True:


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