import glob
import random
import sys, pygame,itertools,time

pygame.display.set_caption('Platform')

class Game(pygame.sprite.Sprite):

    def __init__(self, width, height):
        self.width = width
        self.height = height


        self.window = pygame.display.set_mode((width,height))
        self.standB_Value = (620-85)

        self.xxx = 50
        self.yyy = self.standB_Value

        self.clock = pygame.time.Clock()

        self.stand_bool = True

        self.running_value = 0
        self.runningSprites = ['S:/platform/running\\running1.png',
                               'S:/platform/running\\running2.png', 'S:/platform/running\\running3.png',
                               'S:/platform/running\\running4.png', 'S:/platform/running\\running5.png',
                               'S:/platform/running\\running6.png', 'S:/platform/running\\running7.png',
                               'S:/platform/running\\running8.png', 'S:/platform/running\\running9.png',
                               'S:/platform/running\\running10.png', 'S:/platform/running\\running11.png']
        self.left_running = ['s:/platform/leftrunning\\leftrunning0.png',
         's:/platform/leftrunning\\leftrunning1.png',
         's:/platform/leftrunning\\leftrunning10.png',
         's:/platform/leftrunning\\leftrunning2.png',
         's:/platform/leftrunning\\leftrunning3.png',
         's:/platform/leftrunning\\leftrunning4.png',
         's:/platform/leftrunning\\leftrunning5.png',
         's:/platform/leftrunning\\leftrunning6.png',
         's:/platform/leftrunning\\leftrunning7.png',
         's:/platform/leftrunning\\leftrunning8.png',
         's:/platform/leftrunning\\leftrunning9.png']



        self.stand_time = time.time()
        self.stand_Endtime = time.time()


    def right_running(self,value='right'):

        if self.running_value<len(self.runningSprites)-1:
            self.running_value+=1


        else:
            self.running_value = 0

        if value=='right':
            running = pygame.image.load(self.runningSprites[self.running_value])
            self.window.blit(running,(self.xxx,self.yyy))
            pygame.display.flip()
        else:
            running = pygame.image.load(self.left_running[self.running_value])
            self.window.blit(running, (self.xxx, self.yyy))
            pygame.display.flip()




    def background(self):
        background = pygame.image.load('S:/platform/background.png')
        self.window.blit(background,(0,0))


    def stairs(self):
        stairs = pygame.image.load('S:/platform/grass.png')
        for _ in itertools.chain([0,300,600,900,1200]):
            self.window.blit(stairs,(_,620))


    def grass_stand(self):
        background = pygame.image.load(r's:/platform/stand/stand.png')
        self.window.blit(background,(self.xxx,self.standB_Value))



    def runn_out_RofCheck(self):
        if self.xxx<self.width-(67+40):
            return True

        return False

    def runn_out_LofCheck(self):
        if 0<self.xxx-40:
            return True

        return False



    def timeing_of_character(self):
        # stand_timeing Handled
        if (time.time()-self.stand_time)>0.2712076663970947:
                self.grass_stand()



    


    def mainloop(self):



        while True:
            pygame.time.delay(80)
            self.background()
            self.stairs()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.KEYDOWN:

                    if event.key==pygame.K_RIGHT:
                        self.stand_bool = False
                        if (self.runn_out_RofCheck()):
                            self.xxx+=40
                        self.right_running()

                        self.stand_time = time.time()



                    if event.key==pygame.K_LEFT:
                        self.stand_bool = False

                        if (self.runn_out_LofCheck()):
                            self.xxx-=40
                        self.right_running('left')



                    self.stand_time = time.time()



            # Stairs
            self.stairs()

            self.timeing_of_character()

            #running
            pygame.display.flip()
            self.clock.tick(60)



game = Game(*(1200,650))

if __name__ == '__main__':
    game.mainloop()







