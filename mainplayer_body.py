import glob

import pygame

class times:

    def __init__(self):
        self.jump_clock = False

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
        self.floor_click  = False


class images:

    def __init__(self):
        self.background = pygame.image.load('S:/Mage/game_background.png')

        self.rrun = glob.glob("S:/Mage/Run/*.png")
        self.lrun = glob.glob("S:/Mage/Leftrun/*.png")

        self.rjump = glob.glob("S:/Mage/Jump/*.png")
        self.ljump = glob.glob("S:/Mage/Leftjump/*.png")


        self.rstander = pygame.image.load("S:\Mage\Walk\walk6.png")
        self.lstander = pygame.image.load(self.lrun[7])


class body:

    def __init__(self):
        pass


    def display_background(self,display):
        display.blit(images.background,(0,0))



    def xxx_axismover(self,main_window):
        mainplayer_body.display_background(main_window)


        if body_values.last_press=="Right":

                body_values.xxx_axisvalue+=10
                main_window.blit(pygame.image.load(images.rrun[body_values.Running_movevalue]),
                                 (body_values.xxx_axisvalue,body_values.yyy_axisvalue))


        elif body_values.last_press=="Left":
            body_values.xxx_axisvalue-=10
            main_window.blit(pygame.image.load(images.lrun[body_values.Running_movevalue]),
                             (body_values.xxx_axisvalue, body_values.yyy_axisvalue))


        body_values.Running_movevalue+=1

        if not (body_values.Running_movevalue< len(images.rrun)):
            body_values.Running_movevalue = 0



    def up_downCharactershower(self,main_window,image,value = 0 ):
        main_window.blit(pygame.image.load(image[value]),(body_values.xxx_axisvalue-20,body_values.yyy_axisvalue+20))




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

        if (((body_values.xxx_axisvalue>140 and body_values.xxx_axisvalue<400) or
             (body_values.xxx_axisvalue>=730 and body_values.xxx_axisvalue<(750+250)))
                and (body_values.yyy_axisvalue==(470-120))):

            body_values.floor_stand = True

        else:
            body_values.floor_stand = False


mainplayer_body  = body()
body_values = body_values()
images = images()

