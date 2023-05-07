import os,time,glob
from PIL import Image
import pygame



class timeing:

    def __init__(self):
        self.stand_timer = False
        self.jump_timer = False
        self.jump_run = False




class value_of_characters():
    def __init__(self):

        self.x_move = 300
        self.y_move = (660-60)
        self.last_key = "Right" #using don't delete
        self.running_value = 0
        self.stand = True
        self.y_axis_downing = 0
        self.value_600 = True
        self.jump_runCount = 0 ;

        self.jump_limit = True





class sprites:

    def __init__(self):
        self.lrunning_sprite = glob.glob("S:/platform/rogue/LeftWalk/*.png")
        self.rrunning_sprite = glob.glob("S:/platform/rogue/Walk/*.png")

        self.ljump_sprite = glob.glob("S:/platform/rogue/LeftJump/*.png")
        self.rjump_sprite = glob.glob("S:/platform/rogue/Jump/*.png")


        self.ljump_runn_sprite = pygame.image.load(self.ljump_sprite[3])
        self.rjump_runn_sprite = pygame.image.load(self.rjump_sprite[3])


        print(self.ljump_runn_sprite)
        print(self.rjump_runn_sprite)


class character(pygame.sprite.Sprite):
    def __init__(self,image_path,x_move,y_move):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x_move
        self.rect.y= y_move
        self.group = pygame.sprite.Group()




class character_sprites:


    def icon(self):
        icon = pygame.image.load("S:\platform\Rogue\icon.png")
        pygame.display.set_icon(icon)




    def background(self,platform):
        background = pygame.image.load(r"S:\platform\Rogue\Cartoon_Forest_BG_04.png")
        platform.blit(background, (0, 0))




    def stand(self,platform):

        if (value.stand):


            self.background(platform)
            if (value.last_key=="Right"):
                image = pygame.image.load(character_png.rrunning_sprite[0])
                platform.blit(image,(value.x_move-60,value.y_move-30))

            else:
                image = pygame.image.load(character_png.lrunning_sprite[0])
                platform.blit(image, (value.x_move - 90, value.y_move - 30))

            value.stand = False


    def y_upping(self,platform):
        character_sprite.background(platform=platform)
        value.y_move-=60

        if (value.last_key=="Right"):
            image = character_png.rjump_sprite[0]
            platform.blit(pygame.image.load(image), (value.x_move - 60, value.y_move - 30))

        else:
            image = character_png.ljump_sprite[0]
            platform.blit(pygame.image.load(image), (value.x_move - 90, value.y_move - 30))



    def y_downing(self,platform):
        self.background(platform)


        if (value.last_key == "Right"):
            image = character_png.rjump_sprite[value.y_axis_downing]
            platform.blit(pygame.image.load(image), (value.x_move - 60, value.y_move - 30))

        else:
            image = character_png.ljump_sprite[value.y_axis_downing]
            platform.blit(pygame.image.load(image), (value.x_move - 90, value.y_move - 30))

        if (value.y_axis_downing<4):
            value.y_axis_downing+=1

        else:
            value.y_axis_downing = 3




    def x_moveing(self,platform):

        character_sprite.background(platform)

        if (value.last_key == 'Right'):
           value.x_move+=20
           image = character_png.rrunning_sprite[value.running_value]
           platform.blit(pygame.image.load(image),(value.x_move-60,value.y_move-30))


        elif (value.last_key == 'Left'):
            value.x_move-=20
            image = character_png.lrunning_sprite[value.running_value]
            platform.blit(pygame.image.load(image),(value.x_move-90,value.y_move-30))



        if (value.running_value<len(character_png.rrunning_sprite)-1):
            value.running_value+=1
        else:
            value.running_value = 0



    def standChecking(self):
        if (value.x_move>=200 and value.x_move<=200+30*8) and (value.y_move==540-120) or\
                ((value.x_move>=500 and value.x_move<=540)  and (value.y_move==480-120)):
            value.value_stand = True
            value.count = 0
            value.standJumpCount = 0



        else:
            value.value_stand = False

    def up_checking(self):
        if ((value.x_move >= 200 and value.x_move <= 200 + 30 * 8) and (value.y_move == 500-80)):
            value.do_go_up = True

    def tile1(self,platform):
        for x in range(20):
            platform.blit(pygame.image.load(r'S:\platform\Rogue\ground.png'), (60 * x, 680))



    def smalltile1(self,platform):
        platform.blit(pygame.image.load(
            r"C:\Users\mahen\Downloads\craftpix-781131-free-swamp-game-tileset-pixel-art\1 Tiles\Tile_52.png"),
                         (500, 440))


value = value_of_characters()
character_png = sprites()
timer = timeing()
character_sprite = character_sprites()

















#-----------character---------------



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
#
# for index,_ in enumerate(sprite.attackE):
#     image = Image.open(_)
#     image.resize((90,80)).save(f'S:\platform\Rogue\enemy\enemy{index}.png')


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