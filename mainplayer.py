import pygame,time
from mainplayer_body import  mainplayer_body,body_values,images,times

class main_window(object):


    def __init__(self,width:int ,height:int,title:str):
        self.display = pygame.display.set_mode((width,height))
        pygame.display.set_caption("RogueXWar")
        pygame.display.set_icon(pygame.image.load('S:/platform/Rogue/icon.png'))
        

    def events(self):

        key = pygame.key.get_pressed()

        if body_values.floor_stand:
            body_values.after_jumpmovelimit = 0

        if (key[pygame.K_LEFT] and body_values.yyy_axisvalue==570) \
                or (key[pygame.K_LEFT] and body_values.downed and body_values.after_jumpmovelimit<6):

            body_values.last_press = "Left"

            if (body_values.downed):

                if not body_values.floor_stand:
                    body_values.after_jumpmovelimit += 1
                    body_values.xxx_axisvalue-=20
                    body_values.downed = False

                else:
                    mainplayer_body.xxx_axismover(self.display)
                    body_values.after_jumpmovelimit = 0



            elif not (body_values.downed):
                mainplayer_body.xxx_axismover(self.display)


        elif (key[pygame.K_RIGHT] and body_values.yyy_axisvalue==570) \
                or (key[pygame.K_RIGHT] and body_values.downed and body_values.after_jumpmovelimit<6):



            body_values.last_press = "Right"


            if (body_values.downed):

                if not body_values.floor_stand:
                    # jab stand nahi hoga tab ye wala chalega
                    body_values.downed = False
                    body_values.after_jumpmovelimit += 1
                    body_values.xxx_axisvalue += 20


                else:
                    mainplayer_body.floor_standing()
                    mainplayer_body.xxx_axismover(self.display)

                    #jab floor pe theharega ye wala chalega


            elif not(body_values.downed):
                mainplayer_body.xxx_axismover(self.display)



        elif key[pygame.K_UP]:
            body_values.jumped = True
            body_values.jumping_movevalue = body_values.yyy_axisvalue-300


        else:

            if body_values.jumped:

                if body_values.jumping_movevalue!= body_values.yyy_axisvalue:
                    mainplayer_body.yyy_upmover(self.display)
                    body_values.yyy_axisvalue -= 20


                else:
                    body_values.jumped = False

            else:

                mainplayer_body.floor_standing()

                if body_values.yyy_axisvalue!=570:

                    body_values.downed = True

                    if not (body_values.floor_stand):
                        mainplayer_body.yyy_downmover(self.display)
                        body_values.yyy_axisvalue += 20


                    else:
                        mainplayer_body.stander(self.display)


                else:
                    mainplayer_body.display_background(self.display)
                    mainplayer_body.stander(self.display)
                    body_values.after_jumpmovelimit = 0


    def mainloop(self):
        mainplayer_body.display_background(self.display)
        self.display.blit(pygame.image.load(images.rrun[7]),(body_values.xxx_axisvalue,body_values.yyy_axisvalue))

        while True:

            self.events()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()



            for _ in range(8):
                self.display.blit(pygame.image.load(r"S:\tile.png"),
                                  (200+30*_,570-110))


            for _ in range(8):
                self.display.blit(pygame.image.load(r'S:/tile.png'),
                                  (800+30*_,570-110))


            pygame.display.flip()

player = main_window(1200,700,'RoguexWar')

if __name__ == "__main__":
    player.mainloop()