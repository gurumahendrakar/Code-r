import time,os
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

        character_sprite.tile1_StandChecking()
        # Stand Timer

        #0.1803434343434

        if (time.time() - timer.runnT) < 0.1803434343434:
            print('main to chanlonga')
            character_sprite.x_moveing(self.window)


        else:
            character_sprite.stand(self.window)



    def mainloop(self):
        character_sprite.icon()
        character_sprite.background(self.window)



        while True:
            pygame.time.delay(70)

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    pygame.quit()


                if event.type==pygame.KEYDOWN:

                    if event.unicode=='a':

                        if 800>value.y_move:
                            value.y_move+=50


                        if (value.attack_value<len(sprite.rattack_sprite)-1):
                            value.attack_value+=1

                        else:
                            value.attack_value = 0




                        character_sprite.attack(self.window)
                        timer.attack_timer = time.time()



                    if event.key==pygame.K_RIGHT:

                        character_sprite.tile1_StandChecking()


                        if ( (value.standed) or (value.y_move==800)):
                            pass

                        else:
                            value.y_move+=10



                        if (value.running_value<len(sprite.rrunning_sprite)-1):
                            value.running_value +=1

                        else:
                            value.running_value = 0


                        value.last_key = 'Right'

                        if character_sprite.tile_RightChecking():
                            pass

                        else:
                            value.x_move += 30

                        timer.runnT = time.time()
                        timer.up_timer = time.time()
                        
                        value.stand_ = True



                    if event.key==pygame.K_LEFT:

                        character_sprite.tile1_StandChecking()

                        if (value.running_value<len(sprite.rrunning_sprite)-1):
                            value.running_value +=1

                        else:
                            value.running_value = 0


                        value.last_key = "Left"

                        if character_sprite.tile1_LeftChecking():
                            pass


                        else:
                            value.x_move-=30

                        timer.runnT = time.time()
                        value.stand_ =  True


                    if (time.time()-timer.up_timer)> 0.7803434343434:
                        if (event.key==pygame.K_UP):
                            value.jump = True
                            value.down = False


                            timer.jump_timer = time.time()
                            timer.up_timer = time.time()



            if not (value.jump):

                character_sprite.tile1_StandChecking()

                if (value.standed==False):
                    value.jump = True


                self.sprite_timeing()

                value.down = False

                if (time.time()-timer.attack_timer)>0.08534534534534:
                    value.attack_value=0



                else:
                    character_sprite.attack(self.window)


            else:


                if not (value.down):
                    if (time.time()-timer.jump_timer)>0.2022234343343:
                        value.down = True
                        timer.down_timer = time.time()

                    else:
                            if character_sprite.tile1_UpChecking():
                                value.down = True

                            else:

                                value.y_move -= 100

                                if (time.time() - timer.attack_timer) < 0.1803434343434:
                                    character_sprite.attack(self.window)

                                else:
                                    character_sprite.jump_down_moveing(self.window)


                else:

                    character_sprite.tile1_StandChecking()

                    if value.y_move>850:
                        value.y_move  = 800


                    if not (value.standed) and (value.y_move!=800):

                            if (time.time()-timer.attack_timer)< 0.0803434343434:
                                character_sprite.attack(self.window)




                            else:
                                if (time.time()-timer.runnT)<0.1803434343434:
                                    character_sprite.background(self.window)

                                    image = pygame.image.load(sprite.rjump_sprite[5])
                                    self.window.blit(image,(value.x_move-60,value.y_move-30))



                                else:

                                    value.y_move += 100

                                    if value.y_move>800:
                                        value.y_move = 800
                                    character_sprite.jump_down_moveing(self.window)


                    else:
                        value.jump = False


            self.window.blit(self.tile,(300,485))
            self.window.blit(self.tile,(700,485))
            print(value.x_move,value.y_move)
            pygame.time.Clock().tick(30)
            pygame.display.flip()


plat = platfrom1(1200,900)

if __name__=='__main__':
    plat.mainloop()