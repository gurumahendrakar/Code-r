import time
import numpy as np
import pygame
from Player import playeer
import os
import winsound
pygame.font.init()
class game:

    def __init__(self):
        self.width = 1280
        self.height = 725
        self.window = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_icon(pygame.image.load(r"S:\icon\icon.jpg"))
        pygame.display.set_caption('DeathMode')

        self.image_x = 0
        self.image_y = 1280

        self.surface = pygame.Surface((20,20))
        self.surface.fill('green')

        self.clock = pygame.time.Clock()


        self.key = None
        self.jump = False
        self.right = False
        self.left = False
        self.down = False
        self.fire = False
        self.fire_Pstand = False

        self.time_jump = 0
        self.time_jump1 = 0

        self.time_left = 0
        self.time_left1 = 0

        self.time_right = 0 #right
        self.time_right1 = 0 # right


        self.fire_time = 0
        self.fire_time1 = 0

        self.Mountain_StandingCheck = True


        self.mountain_randomx = np.random.choice(np.arange(500,800,10))
        self.mountain_randomy = np.random.choice(np.arange(300,380,10))


        self.mountain_randomxx = np.random.choice(np.arange(100,300,10))
        self.mountain_randomyy = np.random.choice(np.arange(300,380,10))


        self.mountain1_leftrange = False

        self.bodyfire_time = 0
        self.use_value = 0


        self.enemy_dead = True
        self.enemy_dead_time  = 0


        self.coins= 0
        self.font = pygame.font.SysFont('gamefont.ttf',25)


        self.coins1 = np.linspace(start=self.mountain_randomx,stop=self.mountain_randomx+200 ,dtype=int,num=10)
        self.coins2 = np.linspace(start=self.mountain_randomxx,stop=self.mountain_randomxx+200 ,dtype=int,num=10)

        self.dubli_coins1 = self.coins1.copy()
        self.dubli_coins2 = self.coins2.copy()

        self.increase_mountain = 0


    def background(self):


        self.window.blit(pygame.image.load('S:/HTML/bg.jpg'),(self.image_x,0))
        self.image_x-=5
        self.window.blit(pygame.image.load('S:/HTML/bg.jpg'), (self.image_y, 0))
        self.image_y-=5

        if self.image_x<-1280:
            self.image_x = 1280

        if self.image_y<-1280:
            self.image_y=1280

    def _mainloop(self):
        while True:
            self.background()

            for event in pygame.event.get():



                if event.type==pygame.QUIT:
                    exit()

                if event.type==pygame.KEYDOWN:
                    playeer.left_rightrange_checker(gamee)


                    if not self.fire:
                        if event.unicode=='a':
                            playeer.shoot_x = playeer.xxx+120


                            self.fire_Pstand = True
                            self.fire_time = time.time()
                            self.fire = True
                        else:
                            self.fire_Pstand = False



                    if event.key==pygame.K_UP:
                        self.time_jump = time.time()
                        self.jump = True

                        if playeer.yyy>0:
                            if playeer.xxx>=self.mountain_randomx-70 and playeer.xxx<self.mountain_randomx+170 and playeer.yyy>self.mountain_randomy and \
                                    playeer.yyy<self.mountain_randomyy+210 or playeer.xxx>=self.mountain_randomxx-70 and playeer.xxx<self.mountain_randomxx+180 and playeer.yyy>self.mountain_randomy and \
                                    playeer.yyy<self.mountain_randomyy+210:

                                pass
                            elif playeer.xxx>self.mountain_randomxx+192-45 and playeer.xxx<self.mountain_randomxx+(150+70) and playeer.yyy>self.mountain_randomyy and playeer.yyy<self.mountain_randomyy+80 or \
                                playeer.xxx>self.mountain_randomx+192-45 and playeer.xxx<self.mountain_randomx+(150+70) and playeer.yyy>self.mountain_randomy and playeer.yyy<self.mountain_randomy+80:

                                pass


                            else:
                                playeer.yyy = playeer.yyy-50




                    if event.key==pygame.K_RIGHT and not playeer.no_more_right:

                        if playeer.xxx>self.width//2:
                            self.increase_mountain+=30
                            print(self.increase_mountain)

                        self.key = event.key
                        if playeer.yyy<590-5-50:
                            self.time_right = time.time()
                            self.right =True
                            playeer.running(self.window,4)

                            if playeer.xxx<1140 and playeer.yyy>10:
                                playeer.xxx+=30


                        else:
                            if playeer.xxx<1170:
                                playeer.xxx+=30

                    if event.key==pygame.K_LEFT and not playeer.no_more_right:

                        self.key = event.key

                        if playeer.yyy<590-5-50 and playeer.yyy>0:
                            self.time_left = time.time()
                            self.left = True


                        if playeer.xxx>0 and playeer.yyy>10:
                            playeer.xxx-=30

                    if event.key== pygame.K_DOWN:
                        self.down = True




# ----------------------------------------------jump & stand & down---------------------------------------------------------------------------

            if self.jump and playeer.yyy<590-5 and not self.right and not  self.left and not self.fire_Pstand: # upare jaaa raha hai rha character
                playeer.left_rightrange_checker(gamee) # player ko pahad se aage nahi jaane de raha hai

                if self.key==pygame.K_RIGHT:
                    self.window.blit(pygame.image.load("S:/jumping/jumping4.png"),(playeer.xxx,playeer.yyy))
                elif self.key==pygame.K_LEFT:
                    self.window.blit(pygame.image.load("S:/jumping/leftjumping.png"),(playeer.xxx,playeer.yyy))
                else:
                    self.window.blit(pygame.image.load("S:/jumping/jumping4.png"),(playeer.xxx,playeer.yyy))




            if playeer.yyy<590-5 and not self.right and not self.left and not self.jump and not self.Mountain_StandingCheck and not self.fire_Pstand: # charcter niche aa raha hai

                playeer.character_downing(gamee)




            if playeer.mountain1_Value and not self.right and not self.left and not self.jump and self.Mountain_StandingCheck and not self.fire_Pstand:
                if self.key==pygame.K_LEFT:
                    self.window.blit(pygame.image.load(r"S:/stand/leftstand.png"),(playeer.xxx,playeer.yyy+5))         # mountain pe stand karenge to ye stand work karega

                elif self.key==pygame.K_RIGHT:
                    self.window.blit(pygame.image.load(r"S:/stand/stand.png"),(playeer.xxx,playeer.yyy+5))


            elif (playeer.yyy>590 or playeer.yyy==590) and not  self.right and not  self.fire_Pstand: # 590-5 ke upar ya 590-5 pe stand karega sirf
                playeer.stand(self.window,gamee)
                self.mountain1_leftrange = False

            if self.fire_Pstand:

                if self.use_value==0:
                    self.bodyfire_time = time.time()

                self.use_value = 1

                if time.time()-self.bodyfire_time>0.3201868724822998:
                    self.fire_Pstand = False
                    self.use_value = 0

#-----------------------------------------------------------------------------------------------------------------------


#----------------------------------------- Charcter ko thodi der ruka raha ho yaha pe  ------------------------------------------------------------------
            if self.right and not self.fire_Pstand:
                playeer.left_rightrange_checker(gamee)
                self.time_right1 = time.time()

                if (self.time_right1 - self.time_right)>0.2201868724822998:
                    self.right = False
                else:
                    playeer.running(self.window,4)
                    if playeer.yyy<590-5:

                        if not self.Mountain_StandingCheck:

                            playeer.yyy+=10

                        else:
                            pass

            if self.left and not self.fire_Pstand:

                self.time_left1  = time.time()

                if (self.time_left1 - self.time_left)>0.2201868724822998:
                    self.left = False

                else:
                    self.window.blit(pygame.image.load("S:/leftrunning/running3.png"), (playeer.xxx, playeer.yyy+20))
                    if playeer.yyy<590-5:

                        if not self.Mountain_StandingCheck:
                            playeer.yyy+=10

                        else:
                            pass

            if self.jump and not self.fire_Pstand:
                self.time_jump1 = time.time()

                if (self.time_jump1-self.time_jump)>0.2001868724822998:
                    self.jump = False





            if not playeer.enemie_Dead:
                if (time.time()-playeer.enemie_time)>0.5047635078430176:    # small snake ko sambhal raha ho yaha pe
                    playeer.ChangePosition = False




                else:
                    if playeer.snake_left:
                        self.window.blit(pygame.image.load('S:/enemie/left.png'),(playeer.enemie_move,660-30))  # snake sambhai raha ho yaha pe

                    else:
                        self.window.blit(pygame.image.load('S:/enemie/right.png'),(playeer.enemie_move,660-30))
                    playeer.ChangePosition = True


            if self.fire_Pstand:
                if self.Mountain_StandingCheck:
                    playeer.shootplayer(gamee,playeer.yyy+25)
                else:
                    playeer.shootplayer(gamee,playeer.yyy)
                if playeer.yyy<590-5 and not self.Mountain_StandingCheck:
                    playeer.yyy+=10

            if self.fire:
                if self.key==pygame.K_RIGHT:
                    if playeer.shoot_x<1260:

                        playeer.shoot(gamee)
                        playeer.shoot_x+=30

                    else:
                        self.fire = False
                        playeer.shoot_x = playeer.xxx

                elif self.key==pygame.K_LEFT:
                    if playeer.shoot_x!=0:
                        playeer.shoot(gamee)
                       
                        playeer.shoot_x-=30
                    else:
                        self.fire = False
                        playeer.shoot_x = playeer.xxx


                else:
                    if playeer.shoot_x<1260:
                        playeer.shoot(gamee)
                        playeer.shoot_x+=30

                    else:
                        self.fire = False
                        playeer.shoot_x = playeer.xxx


            if not self.enemy_dead:
                if time.time()-self.enemy_dead_time<0.5047635078430176:
                    self.window.blit(pygame.image.load('s:/sleep/sleep.png'),(playeer.enemie_move,695-30))



#------------------------------------------------------------------------------------------------------



            if playeer.xxx+60==playeer.enemie_move and playeer.yyy==590:
                playeer.xxx  = 30


            if self.enemy_dead:

                if playeer.shoot_x==playeer.enemie_move and playeer.yyy==590:
                    self.enemy_dead_time = time.time()
                    self.enemy_dead = False

                



            if self.enemy_dead:
                playeer.enemies(gamee)



            self.rendering = self.font.render(f'Coins : {self.coins}',True,'#ffe6e6',None)

            playeer.coin(gamee)
            playeer.coins_takeing(gamee)

            playeer.left_rightrange_checker(gamee)
            playeer.mountain1(self.window,gamee,self.mountain_randomx-self.increase_mountain,self.mountain_randomy,"S:/floor/flo.png")
            playeer.mountain1(self.window,gamee,self.mountain_randomxx,self.mountain_randomyy,"S:/floor/flo.png")
            playeer.mountain1(self.window,gamee,self.mountain_randomx+192,self.mountain_randomy+40,'S:/floor/floor.png')
            playeer.mountain1(self.window,gamee,self.mountain_randomxx+192,self.mountain_randomyy+40,'S:/floor/floor.png')
            playeer.mountain1_standC(gamee)
            
        


            self.window.blit(pygame.image.load(r"S:/floor/grass.png"),(0,700)) # Grass rendering

            self.window.blit(self.rendering,(1180,10))

            pygame.display.flip()
            self.clock.tick(60)
            



gamee = game()
if __name__ == '__main__':
    gamee._mainloop()
