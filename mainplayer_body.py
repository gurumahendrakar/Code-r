import glob,re,time
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
        self.attack_movevalue = 0


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

        self.downing_attack_count = False

        self.fire_on = False
        self.fire_value = 0
        self.fire_list = []


        self.enemy_movevalue = 0
        self.enemy_positiongoing = "Right"
        self.move_enemy = True
        self.move_time = False
        self.enemy_dead = False





class images:

    def __init__(self):
        self.background = pygame.image.load(r"S:/Mage/game_background.jpg")

        self.rrun = glob.glob("S:/Mage/Run/*.png")
        self.lrun = glob.glob("S:/Mage/Leftrun/*.png")

        self.rjump = glob.glob("S:/Mage/Jump/*.png")
        self.ljump = glob.glob("S:/Mage/Leftjump/*.png")


        self.rstander = pygame.image.load("S:\Mage\Walk\walk6.png")
        self.lstander = pygame.image.load("S:\Mage\Walk\leftwalk.png")

        self.lattack =  glob.glob('S:\Mage\Leftattack\*.png')
        self.rattack = glob.glob('S:/Mage/Attack/*.png')

        self.coin_image = pygame.image.load("S:/Mage/coin.png")



        self.fire = pygame.image.load('S:/Mage/Fire/fire2.png')


        self.small_tile = pygame.image.load('S:/Mage/tile.png')
        self.bigtile = pygame.image.load('S:/Mage/tilee.png')



        self.lenemy_run = glob.glob('S:\Mage\leftenemy\*.png')
        self.renemy_run = glob.glob('S:/Mage/enemy/*.png')




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


        if body_values.last_press=="Left" and body_values.floor_stand:
            main_window.blit(images.lstander,(body_values.xxx_axisvalue-20,body_values.yyy_axisvalue))

        elif body_values.last_press=="Left":
            main_window.blit(images.lstander, (body_values.xxx_axisvalue, body_values.yyy_axisvalue))


        elif body_values.last_press=="Right":
            main_window.blit(images.rstander,(body_values.xxx_axisvalue,body_values.yyy_axisvalue))



    def floor_standing(self):

        if body_values.last_press=="Left":

            # bigtile standing comparision check
            if (((body_values.xxx_axisvalue>100 and body_values.xxx_axisvalue<330) or
                 (body_values.xxx_axisvalue>700 and body_values.xxx_axisvalue<(710+200))) # big 2 tiles
                    and (body_values.yyy_axisvalue==(470-120))) \
                    \
                    \
                    or (body_values.xxx_axisvalue >450-80  and body_values.xxx_axisvalue < 440) and body_values.yyy_axisvalue == 270-120 \
                                                    or\
                    \
                    ((body_values.xxx_axisvalue>550-80 and body_values.xxx_axisvalue<540) and body_values.yyy_axisvalue==170-120) \
                                                    or \
                    (body_values.xxx_axisvalue>(1012-100) and body_values.xxx_axisvalue<(1012+200)) and body_values.yyy_axisvalue==90:


                body_values.floor_stand = True
                body_values.floor_click = False
                body_values.attack_clicked = False


            else:

                body_values.floor_click = True
                body_values.floor_stand = False



        elif body_values.last_press=="Right":


            if (((body_values.xxx_axisvalue > (120+20) and body_values.xxx_axisvalue < 360) or
                 (body_values.xxx_axisvalue > 740 and body_values.xxx_axisvalue < (710 + 260)))
                    and (body_values.yyy_axisvalue == (470 - 120))) \
                    \
                    \
                    or (body_values.xxx_axisvalue >450-50  and body_values.xxx_axisvalue < 450)\
                    and body_values.yyy_axisvalue == 270-120 or \
                    \
                    \
                    (body_values.xxx_axisvalue>500 and body_values.xxx_axisvalue<550) and body_values.yyy_axisvalue==170-120\
                                                        or \
 \
                    (body_values.xxx_axisvalue > (1012 - 60) and body_values.xxx_axisvalue < (
                            1012 + 220)) and body_values.yyy_axisvalue == 190-100:


                body_values.floor_stand = True
                body_values.floor_click = False
                body_values.attack_clicked = False




            else:
                body_values.floor_click = True
                body_values.floor_stand = False



    def up_floorChecking(self):

        if body_values.last_press == "Left":

            if (((body_values.xxx_axisvalue > 100 and body_values.xxx_axisvalue < 330) or
                (body_values.xxx_axisvalue > 700 and body_values.xxx_axisvalue < (710+220)))
                    and (body_values.yyy_axisvalue == (470 - 120+40))):
                return True

        elif body_values.last_press == "Right":

            if (((body_values.xxx_axisvalue > 120 + 10 and body_values.xxx_axisvalue < 360) or
                 (body_values.xxx_axisvalue > 740 and body_values.xxx_axisvalue < (710+250)))
                    and (body_values.yyy_axisvalue == (470 - 120 + 40))):
                return True

        return False



    def small_tiles(self,main_window,x_position,y_position):
        main_window.blit(images.small_tile, (x_position, y_position))




    def tile(self,main_window,x_position,y_position):
        main_window.blit(images.bigtile,
                          (x_position,y_position))

    def ground(self,main_window):
        main_window.blit(pygame.image.load(r'S:/Mage/bigtile.png'),(0,680))

    def coins(self,main_window):
        for _ in body_values.tile1_coins:
            main_window.blit(images.coin_image, (_, 270))

        for _ in body_values.tile2_coins:
            main_window.blit(images.coin_image, (_, 270))


    def conditions_of_coins(self,value = 0,increase_length_cointaken = 0 ):
        if (((body_values.xxx_axisvalue > 100  and body_values.xxx_axisvalue < 350)) and body_values.yyy_axisvalue == 270-40):

            length = len(body_values.tile1_coins)

            body_values.tile1_coins = (body_values.tile1_coins[
                (body_values.tile1_coins >= body_values.xxx_axisvalue + value) ^ (
                            body_values.tile1_coins < body_values.xxx_axisvalue + increase_length_cointaken)])

            body_values.coin_score+=  length - len(body_values.tile1_coins)


        elif (body_values.xxx_axisvalue > 710 and body_values.xxx_axisvalue < (
                750 + (230 - 30)) and body_values.yyy_axisvalue == 270-40):
            length = len(body_values.tile2_coins)

            body_values.tile2_coins = (body_values.tile2_coins[
                (body_values.tile2_coins >= body_values.xxx_axisvalue + value) ^ (
                        body_values.tile2_coins < body_values.xxx_axisvalue + increase_length_cointaken)])

            body_values.coin_score += length - len(body_values.tile2_coins)


    def coins_remover(self):

        if body_values.last_press=='Left':
            mainplayer_body.conditions_of_coins(value = 20,increase_length_cointaken=110)

        else:
            mainplayer_body.conditions_of_coins(increase_length_cointaken=80)


    def enemy_deadlogic(self,position):
        if not body_values.enemy_dead:
            if not position%2==0:
                position-=5

            if (enemy_group.rect.x==position):
                print('true')

            else:
                print(enemy_group.rect.x,position,body_values.xxx_axisvalue)



    def enemy_movingshowingoffing(self,main_window):
        if (time.time() - body_values.move_time) > 0.056431356135131351354131354 and not body_values.enemy_dead:  # itne time enemy move nahi karega jaise hi
                                                                                                                    # time bada hogaya old se phir se enemy move                                                                                            # chalta rahega
            enemy.update(main_window)
            body_values.move_time = time.time()


        if (not body_values.enemy_dead):
            enemy.draw(main_window)


    def fire(self,main_window):

        for index,list in enumerate(body_values.fire_list):
            self.enemy_deadlogic(list[0])



            if list[2]=='Left':
                main_window.blit(images.fire, (list[0]-20, list[1]))
                body_values.fire_list[index] = (list[0] - 10, list[1], list[2])
                if not list[0] > 0:
                    body_values.fire_list.remove((list[0] - 10, list[1], list[2]))


            elif list[2]=="Right":

                main_window.blit(images.fire, (list[0] - 20, list[1]))
                body_values.fire_list[index] = (list[0] + 10, list[1],list[2])
                if not list[0] < 1200:
                    body_values.fire_list.remove((list[0] + 10, list[1],list[2]))










class attack_group(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(images.rattack[4])
        self.rect = self.image.get_rect()
        self.rect.topleft = [body_values.xxx_axisvalue,body_values.yyy_axisvalue]



        self.attack_value = 0

    def update(self):

        if body_values.last_press=="Left":

            self.image = pygame.image.load(images.lattack[4])

        elif body_values.last_press=="Right":
            self.image = pygame.image.load(images.rattack[4])











class enemy_sprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(images.renemy_run[body_values.enemy_movevalue])
        self.rect  = self.image.get_rect()
        self.rect.x = 1010-70
        self.rect.y = 200-67


    def update(self,main_window):

        if (len(images.renemy_run)-1) < body_values.enemy_movevalue:
            body_values.enemy_movevalue = 0


        else:
            if body_values.enemy_positiongoing == "Left":
                self.image = pygame.image.load(images.lenemy_run[body_values.enemy_movevalue])


            elif body_values.enemy_positiongoing == "Right":
                self.image = pygame.image.load(images.renemy_run[body_values.enemy_movevalue])



            enemy.add(enemy_group)
            body_values.enemy_movevalue += 1



            if body_values.enemy_positiongoing=='Right':
                enemy_group.rect.x+=10
                if enemy_group.rect.x>1130:
                    body_values.enemy_positiongoing = 'Left'


            elif body_values.enemy_positiongoing=="Left":

                if enemy_group.rect.x ==800:
                    body_values.enemy_positiongoing = "Right"

                enemy_group.rect.x -=10






timer = timer()
mainplayer_body  = body()
body_values = body_values()
images = images()

attack_group = attack_group()
enemy_group = enemy_sprite()

attack = pygame.sprite.Group()
enemy =  pygame.sprite.Group()

attack.add(attack_group)
enemy.add(enemy_group)

