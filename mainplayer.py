import pygame,time
from mainplayer_body import  mainplayer_body,body_values,images,times

class main_window(object):


    def __init__(self,width:int ,height:int,title:str):
        self.display = pygame.display.set_mode((width,height))
        pygame.display.set_caption("RogueXWar")
        pygame.display.set_icon(pygame.image.load('S:/platform/Rogue/icon.png'))
        

    def events(self):

        key = pygame.key.get_pressed()


        if (key[pygame.K_LEFT] and body_values.yyy_axisvalue==570) \
                or (key[pygame.K_LEFT] and body_values.downed):

            if (body_values.downed):
                body_values.xxx_axisvalue-=10

            elif not (body_values.downed):
                body_values.last_press = "Left"
                mainplayer_body.xxx_axismover(self.display)


        elif (key[pygame.K_RIGHT] and body_values.yyy_axisvalue==570) \
                or (key[pygame.K_LEFT] and body_values.downed):

            if (body_values.downed):
                body_values.xxx_axisvalue += 10

            elif not(body_values.downed):
                body_values.last_press = "Right"
                mainplayer_body.xxx_axismover(self.display)


        elif key[pygame.K_UP]:
            body_values.jumped = True


        else:

            if body_values.jumped:

                if 300 != body_values.yyy_axisvalue:
                    print(body_values.xxx_axisvalue, body_values.yyy_axisvalue)
                    body_values.yyy_axisvalue-=10
                    mainplayer_body.yyy_upmover(self.display)


                else:
                    body_values.jumped = False

            else:

                if body_values.yyy_axisvalue!=570:

                    body_values.downed = True

                    body_values.yyy_axisvalue+=10
                    mainplayer_body.yyy_downmover(self.display)

                else:
                    mainplayer_body.display_background(self.display)
                    mainplayer_body.stander(self.display)



    def mainloop(self):
        mainplayer_body.display_background(self.display)
        self.display.blit(pygame.image.load(images.rrun[7]),(body_values.xxx_axisvalue,body_values.yyy_axisvalue))

        while True:

            self.events()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()




            pygame.display.flip()

player = main_window(1200,700,'RoguexWar')

if __name__ == "__main__":
    player.mainloop()