
import itertools
import os
import glob
import time
import numpy as np
import pygame
import winsound





class player:
    def __init__(self):
        self.sprites = ()

        self.left_count = 0
        self.right_count = 0

        self.mountain1_Value = False



        self.xxx = 30
        self.yyy = 590

        self.shoot_x = self.xxx+120

        self.no_more_right  = False

        self.enemie_move,self.x = 990,0

        self.enemie_time = 0
        self.enemie_time1 = 0
        self.ChangePosition = False
        self.snake_left = True

        self.enemie_Dead = False




    def mountain1(self,surface,object,__x,__y,imagepath):
        '''192x228'''

        surface.blit( pygame.image.load(imagepath),(__x,__y))



    def mountain1_standC(self,objectt):
        if self.xxx>objectt.mountain_randomx-100 and self.xxx<objectt.mountain_randomx+240 and self.yyy==objectt.mountain_randomy-90:

            objectt.Mountain_StandingCheck = True
            self.mountain1_Value =  True

        elif self.xxx>objectt.mountain_randomxx-100 and self.xxx<objectt.mountain_randomxx+240 and self.yyy==objectt.mountain_randomyy-90:
            objectt.Mountain_StandingCheck = True
            self.mountain1_Value =  True

        else:
            objectt.Mountain_StandingCheck = False


    def running(self,surface,x):
        surface.blit(pygame.image.load(f'S:/running/{os.listdir("S:/running")[x]}'),(playeer.xxx,playeer.yyy+20))


    def stand(self,surface,object):
        if object.key:
            if object.key==pygame.K_RIGHT:

                surface.blit(pygame.image.load("S:/stand/stand.png"),(playeer.xxx,playeer.yyy-20))

            elif object.key==pygame.K_LEFT:
                surface.blit(pygame.image.load("S:/stand/leftstand.png"),(playeer.xxx,playeer.yyy-20))


        else:
            surface.blit(pygame.image.load("S:/stand/stand.png"), (playeer.xxx, playeer.yyy-20))



    def character_downing(self,object):


        playeer.yyy+=10
        if object.key==pygame.K_RIGHT:

            object.window.blit(pygame.image.load("S:/jumping/jumping5.png"),(playeer.xxx,playeer.yyy))
        elif object.key==pygame.K_LEFT:
            object.window.blit(pygame.image.load("S:/jumping/leftjumping.png"),(playeer.xxx,playeer.yyy))

        else:
            object.window.blit(pygame.image.load("S:/jumping/jumping5.png"),(playeer.xxx,playeer.yyy))



    def shoot(self,object):
        if object.key==pygame.K_RIGHT:
            object.window.blit(pygame.image.load('S:/fire/fire.png'),(self.shoot_x+100,playeer.yyy+60))

        elif object.key==pygame.K_LEFT:

            object.window.blit(pygame.image.load('S:/fire/fire.png'),(self.shoot_x-100,playeer.yyy+50))

        else:

            object.window.blit(pygame.image.load('S:/fire/fire.png'),(self.shoot_x+100,playeer.yyy+50))


    #
    def left_rightrange_checker(self,object):

        if (playeer.xxx>(object.mountain_randomx-200) and playeer.xxx<object.mountain_randomx+180) and \
                (playeer.yyy<object.mountain_randomy+180 and playeer.yyy>object.mountain_randomy)  or \
                (playeer.xxx>(object.mountain_randomxx-110) and playeer.xxx<object.mountain_randomxx+180) and \
                (playeer.yyy<object.mountain_randomyy+180 and playeer.yyy>object.mountain_randomyy):


            self.no_more_right = True


        else:
            self.no_more_right = False


    # snake ko position de raha ho
    def enemies(self,object):
        if  not playeer.ChangePosition:

            self.ChangePosition = True
            self.enemie_time = time.time()

            if self.snake_left:
                self.enemie_move-=30
            else:
                self.enemie_move+=30

            if self.enemie_move==690:
                self.snake_left = False

            elif self.enemie_move==990:
                self.snake_left = True


    def shootplayer(self,object,yyy):
        if object.key==pygame.K_LEFT:
                object.window.blit(pygame.image.load(r"S:\fire\leftshootplayer.png"),(playeer.xxx,yyy))

        elif object.key==pygame.K_RIGHT:
                object.window.blit(pygame.image.load(r"S:\fire\shootplayer.png"),(playeer.xxx,yyy))

        else:
            object.window.blit(pygame.image.load(r"S:\fire\shootplayer.png"),(playeer.xxx,yyy))


    # snake image ko sambhal raha ho
    def snake_range(self,object):
        if playeer.yyy==590 and playeer.xxx>600 and playeer.yyy<900:
            object.window.blit(pygame.image.load('S:/snake/fire.png'),(600,590-25))




    def coin(self,object):

        if any(object.coins1):
            for x in range(len(object.coins1)):
                object.window.blit(pygame.image.load(r"S:\coin\coin-removebg-preview (2).png"),(object.coins1[x],object.mountain_randomy-150))



        if any(object.coins2):
            for x in range(len(object.coins2)):
                object.window.blit(pygame.image.load(r"S:\coin\coin-removebg-preview (2).png"),(object.coins2[x],object.mountain_randomyy-150))


    def coins_takeing(self,object):

       if self.xxx>object.mountain_randomxx-100 and self.xxx<object.mountain_randomxx+200 and \
               self.yyy<object.mountain_randomyy-150 or self.xxx>object.mountain_randomx-100 and self.xxx<object.mountain_randomx+200 and \
               self.yyy<object.mountain_randomy-150:
           coins22 = (object.coins2>self.xxx) & (object.coins2<self.xxx+100)
           coins11 = (object.coins1>self.xxx) & (object.coins1<self.xxx+100)


           object.coins2 =np.delete(object.coins2,coins22)
           object.coins1 = np.delete(object.coins1,coins11)
           object.coins+= sum(coins11)
           object.coins+= sum(coins22)






        
playeer = player()






