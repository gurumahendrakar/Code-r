import glob
import numpy as np
import pygame
pygame.font.init()

class timer:

    def __init__(self):
        self.attack_timer = False

class body_values:

    def __init__(self):



        self.last_press = "Right"
        self.xxx_axisvalue = 250
        self.yyy_axisvalue = 700-130



        self.Running_movevalue = 0
        self.jumped = False
        self.downed = False


        self.jumping_movevalue = 0 #jump  upper jaana hai yaha pe batayenge aur otna updar jaake self.jumped ko false kardenge
        self.after_jumpmovelimit = 0


        self.floor_stand = False
        self.floor_click = False


        self.attack_clicked = False


        self.font = pygame.font.SysFont('cascade',size=30)
        self.coin_score = 0

        self.tile1_coins = (np.arange(200, 200 + 30 * 7, step=30))
        self.tile2_coins = (np.arange(800, 800 + 30 * 7, step=30))


        self.tile1coin_remover_array = self.tile1_coins-60
        self.tile2coin_remover_array = self.tile2_coins-60









class images:

    def __init__(self):
        self.background = pygame.image.load('S:/Mage/game_background.jpg')

        self.rrun = glob.glob("S:/Mage/Run/*.png")
        self.lrun = glob.glob("S:/Mage/Leftrun/*.png")

        self.rjump = glob.glob("S:/Mage/Jump/*.png")
        self.ljump = glob.glob("S:/Mage/Leftjump/*.png")


        self.rstander = pygame.image.load("S:\Mage\Walk\walk6.png")
        self.lstander = pygame.image.load("S:\Mage\Walk\leftwalk.png")


        self.rattack = glob.glob('S:/Mage/Attack/*.png')

        self.coin_image = pygame.image.load("S:/Mage/coin.png")

class body:

    def __init__(self):
        pass


    def display_background(self,display):
        display.blit(images.background,(0,0))



    def xxx_axismover(self,main_window):
        mainplayer_body.display_background(main_window)


        if body_values.last_press=="Right":

                body_values.xxx_axisvalue+=5
                main_window.blit(pygame.image.load(images.rrun[body_values.Running_movevalue]),
                                 (body_values.xxx_axisvalue,body_values.yyy_axisvalue))


        elif body_values.last_press=="Left":
            body_values.xxx_axisvalue-=5
            main_window.blit(pygame.image.load(images.lrun[body_values.Running_movevalue]),
                             (body_values.xxx_axisvalue, body_values.yyy_axisvalue))


        body_values.Running_movevalue+=1

        if not (body_values.Running_movevalue< len(images.rrun)):
            body_values.Running_movevalue = 0



    def up_downCharactershower(self,main_window,image,value = 0 ):
        main_window.blit(pygame.image.load(image[value]),(body_values.xxx_axisvalue,body_values.yyy_axisvalue+20))




    def yyy_upmover(self,main_window):
        mainplayer_body.display_background(main_window)

        if body_values.last_press=='Left':
            mainplayer_body.up_downCharactershower(main_window,images.ljump,value=2)

        elif body_values.last_press=="Right":
            mainplayer_body.up_downCharactershower(main_window, images.rjump, value=2)


    def yyy_downmover(self,main_window):
        mainplayer_body.display_background(main_window)


        if body_values.last_press == 'Left':
            mainplayer_body.up_downCharactershower(main_window, images.ljump, value=5)

        elif body_values.last_press == "Right":
            mainplayer_body.up_downCharactershower(main_window, images.rjump, value=5)



    def stander(self,main_window):
        mainplayer_body.display_background(main_window)


        if body_values.last_press=="Left":
            main_window.blit(images.lstander,(body_values.xxx_axisvalue,body_values.yyy_axisvalue))


        elif body_values.last_press=="Right":
            main_window.blit(images.rstander,(body_values.xxx_axisvalue,body_values.yyy_axisvalue))



    def floor_standing(self):

        if body_values.last_press=="Left":
            if (((body_values.xxx_axisvalue>120+10 and body_values.xxx_axisvalue<310) or
                 (body_values.xxx_axisvalue>710 and body_values.xxx_axisvalue<(710+200)))
                    and (body_values.yyy_axisvalue==(470-120))):
                body_values.floor_stand = True
                body_values.floor_click = False
            else:
                body_values.floor_click = True
                body_values.floor_stand = False



        elif body_values.last_press=="Right":
            if (((body_values.xxx_axisvalue > 120+10 and body_values.xxx_axisvalue < 350) or
                 (body_values.xxx_axisvalue > 710 and body_values.xxx_axisvalue < (710 + 250)))
                    and (body_values.yyy_axisvalue == (470 - 120))):
                body_values.floor_stand = True
                body_values.floor_click = False

            else:
                body_values.floor_click = True
                body_values.floor_stand = False



    def up_floorChecking(self):


        if (((body_values.xxx_axisvalue > 120+10 and body_values.xxx_axisvalue < 330) or
            (body_values.xxx_axisvalue > 730 and body_values.xxx_axisvalue < (750 + (230-30))))
                and (body_values.yyy_axisvalue == (470 - 120+40))):
            return True

        return False


    def tile(self,main_window,start,end):
        main_window.blit(pygame.image.load(r"S:/Mage/tilee.png"),
                          (start,end))

    def ground(self,main_window):
        main_window.blit(pygame.image.load(r'S:/Mage/bigtile.png'),(0,680))



    def conditions_of_coins(self,value = 0,increase_length_cointaken = 0 ):
        if (((body_values.xxx_axisvalue > 120 + 10 and body_values.xxx_axisvalue < 330)) and body_values.yyy_axisvalue == 270):
            body_values.tile1_coins = (body_values.tile1_coins[
                (body_values.tile1_coins >= body_values.xxx_axisvalue + value) ^ (
                            body_values.tile1_coins < body_values.xxx_axisvalue + increase_length_cointaken)])


        elif (body_values.xxx_axisvalue > 730 + 10 and body_values.xxx_axisvalue < (
                750 + (230 - 50)) and body_values.yyy_axisvalue == 270):
            body_values.tile2_coins = (body_values.tile2_coins[
                (body_values.tile2_coins >= body_values.xxx_axisvalue + value) ^ (
                        body_values.tile2_coins < body_values.xxx_axisvalue + increase_length_cointaken)])


    def coins_remover(self):

        print(body_values.last_press)

        if body_values.last_press=='Left':
            mainplayer_body.conditions_of_coins(value = 30,increase_length_cointaken=110)

        else:
            mainplayer_body.conditions_of_coins(increase_length_cointaken=80)








class attack_group(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'S:/Mage/Run/run1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [body_values.xxx_axisvalue,body_values.yyy_axisvalue]



        self.attack_value = 0

    def update(self):
        self.image = pygame.image.load(images.rattack[self.attack_value])

        self.attack_value+=1
        if (len(images.rattack)-1<self.attack_value):
            self.attack_value  = 0






timer = timer()
mainplayer_body  = body()
body_values = body_values()
images = images()

attack_group = attack_group()
attack = pygame.sprite.Group()
attack.add(attack_group)
