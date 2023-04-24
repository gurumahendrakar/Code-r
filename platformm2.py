import os,time,glob
from PIL import Image
import pygame



class timeing:

    def __init__(self):
        self.runnT =  False

        self.jump_timer = False
        self.down_timer = False


        self.attack_timer = False


        self.up_timer = False


class value_of_characters():
    def __init__(self):

        self.x_move = 300
        self.y_move = (900-100)


        self.last_key = "Right" #using don't delete
        self.running_value = 0
        self.attack_value = 0
        self.jump = False # using dont`t delete
        self.standed  = False
        self.upClicked = False
        self.down = False

class sprites:

    def __init__(self):
        self.rrunning_sprite = glob.glob("S:/platform/rogue/Walk/*.png")[:-2]
        self.lrunning_sprite = glob.glob("S:/platform/rogue/LeftWalk/*.png")[:-2]

        self.rjump_sprite = glob.glob("S:/platform/rogue/Jump/*.png")
        self.ljump_sprite = glob.glob("S:/platform/rogue/LeftJump/*.png")


        self.rattack_sprite = glob.glob('S:/platform/rogue/Attack/*.png')
        self.lattack_sprite = glob.glob('S:/platform/rogue/LeftAttack/*.png')


        self.attackE= glob.glob(r'C:\Users\mahen\Downloads\craftpix-904589-free-reaper-man-chibi-2d-game-sprites\Reaper_Man_2\PNG\PNG Sequences\Slashing\*.png')
        self.enemy_move = glob.glob(r'C:\Users\mahen\Downloads\craftpix-904589-free-reaper-man-chibi-2d-game-sprites\Reaper_Man_2\PNG\PNG Sequences\Running')



class character(pygame.sprite.Sprite):
    def __init__(self,image_path,x_move,y_move):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x_move
        self.rect.y= y_move
        self.group = pygame.sprite.Group()




class character_sprites:

    def __init__(self):
        pass



    def icon(self):
        icon = pygame.image.load("S:\platform\Rogue\icon.png")
        pygame.display.set_icon(icon)




    def background(self,platform):
        background = pygame.image.load(r"S:\platform\Rogue\game_background_1.png")
        platform.blit(background, (0, 0))




    def stand(self,platform):


        character_sprite.background(platform=platform)

        if (value.last_key == 'Right'):
            stand = pygame.image.load("S:\platform\Rogue\Walk\walk2.png")

        elif (value.last_key == 'Left'):
            stand = pygame.image.load("S:\platform\Rogue\LeftWalk\LeftWalk1.png")



        if value.last_key=="Left":
            platform.blit(stand,(value.x_move-90,value.y_move-30))

        else:
            platform.blit(stand, (value.x_move - 60, value.y_move - 30))



    def ground(self,platform):
        ground = pygame.image.load("S:/platform/Rogue/ground.png")
        platform.blit(ground,(0,900-20))



    def x_moveing(self,platform):
        character_sprite.background(platform)

        if (value.running_value<len(sprite.rrunning_sprite)-1):
            value.running_value+=1
        else:
            value.running_value = 0


        if (value.last_key == 'Right'):
            image = sprite.rrunning_sprite[value.running_value]

        elif (value.last_key == 'Left'):
            image = image = sprite.lrunning_sprite[value.running_value]

        if (value.last_key=='Left'):
            platform.blit(pygame.image.load(image),(value.x_move-90,value.y_move-30))

        else:
            platform.blit(pygame.image.load(image), (value.x_move - 60, value.y_move - 30))



    def attack(self, platform):
        character_sprite.background(platform)

        if value.last_key=='Right':
            image = sprite.rattack_sprite[value.attack_value]
        else:
            image = sprite.lattack_sprite[value.attack_value]


        attack.group.empty()
        attack.group.add(character(image, x_move=value.x_move - 60, y_move=value.y_move - 30))
        attack.group.draw(platform)
        jump.group.update()





    def jump_down_moveing(self, platform):
        character_sprite.background(platform)

        if (value.last_key == 'Right'):
            image = sprite.rjump_sprite[5]

        elif (value.last_key == 'Left'):
            image = sprite.ljump_sprite[5]


        jump.group.empty()

        if (value.last_key=="Left"):
            jump.group.add(character(image,value.x_move - 90, value.y_move - 30))
        else:
            jump.group.add(character(image, value.x_move - 60, value.y_move - 30))


        jump.group.draw(platform)
        jump.group.update()



    def tile1_UpChecking(self):



        if (((value.x_move>=290) and (value.x_move<300+340)) or ((value.x_move>300+400+10) and (value.x_move<700+300+50+10)))\
                and (value.y_move<=320+200 and value.y_move>259+200):

            return True

        return False


    def tile1_StandChecking(self):
        if (((value.x_move >= 290) and (value.x_move < 300 + 350+10)) or (value.x_move>=300+400 and value.x_move<(700+350+10)))\
                and (value.y_move==400):
            value.standed = True

        else:

            value.standed = False


    def tile_RightChecking(self):
        if ((value.x_move>=300 and value.x_move<=310 or (value.x_move>660 and value.x_move<=690)) and
                (value.y_move>=410 and value.y_move<=450)) :

            return True

        return False



    def tile1_LeftChecking(self):
        if ((value.x_move >= 570 and value.x_move <= 630) and (
                value.y_move >= 210 + 200 and value.y_move <= 250 + 200)):
            return True

        return False



value = value_of_characters()
sprite = sprites()
timer = timeing()
character_sprite = character_sprites()



#-----------character---------------
run = character(r"S:\platform\Rogue\Run\run1.png",value.x_move,value.y_move)
jump = character(r"S:\platform\Rogue\Run\run1.png",value.x_move,value.y_move)
attack  =  character(r"S:\platform\Rogue\Run\run1.png",value.x_move,value.y_move)


#
# import cv2
# from PIL import Image
#
#
#
#
# cv2 = cv2.__dict__
#
# os.mkdir(r'S:\platform\Rogue\LeftAttack')
# for index,_ in enumerate(glob.glob("s:/platform/Rogue/Attack/*.png")):
#     image = Image.open(_)
#     (image.transpose(method=Image.FLIP_LEFT_RIGHT)
#      .save(fr"S:\platform\Rogue\LeftAttack\LeftAttack{index}.png"))


# image resize
#

for index,_ in enumerate(sprite.attackE):
    image = Image.open(_)
    image.resize((90,80)).save(f'S:\platform\Rogue\enemy\enemy{index}.png')


#
# image = Image.open('s:/platform/ninja/stand/stand.png')
# image.resize((50,80)).save(f's:/platform/ninja/stand/stand.png')


#
#
# cv2 = cv2.__dict__
#
# im1 = cv2['imread'](r"C:\Users\mahen\Downloads\craftpix-net-753737-free-green-zone-tileset-pixel-art (1)\1 Tiles\Tile_01.png")
# im2 = cv2['imread'](r"C:\Users\mahen\Downloads\craftpix-net-753737-free-green-zone-tileset-pixel-art (1)\1 Tiles\Tile_01.png")
#
#
#
# c = cv2['hconcat']([im1]*8)
#
#
# cv2['imwrite'](r'S:\Code-r\sexy.png',c)
#
#
# cv2['waitKey'](5000)