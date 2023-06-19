import pygame,time
from mainplayer_body import  mainplayer_body,body_values,images,attack,attack_group,timer,enemy_group,enemy

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
                or (key[pygame.K_LEFT] and body_values.downed and body_values.after_jumpmovelimit<7):

            body_values.last_press = "Left"

            if (body_values.downed):

                if not (body_values.floor_stand):
                    body_values.after_jumpmovelimit += 1
                    body_values.xxx_axisvalue-=20
                    mainplayer_body.yyy_downmover(self.display)
                    body_values.downed = False

                else:
                    mainplayer_body.floor_standing()
                    mainplayer_body.xxx_axismover(self.display)
                    body_values.after_jumpmovelimit = 0



            elif not (body_values.downed):
                mainplayer_body.xxx_axismover(self.display)



        elif (key[pygame.K_RIGHT] and body_values.yyy_axisvalue==570) \
                or (key[pygame.K_RIGHT] and body_values.downed and body_values.after_jumpmovelimit<7):



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



        elif (((key[pygame.K_UP] and (body_values.yyy_axisvalue==570)) or (key[pygame.K_UP] and  not body_values.floor_click)) \
                and not body_values.jumped):

            body_values.jumped = True
            body_values.jumping_movevalue = body_values.yyy_axisvalue-300



        elif ((((key[pygame.K_a]  and not body_values.attack_clicked))
               and (not  body_values.jumped) and not body_values.downed)) or \
                ((key[pygame.K_a] and body_values.floor_stand and not body_values.attack_clicked) and not body_values.jumped):

            attack_group.rect.x,attack_group.rect.y = body_values.xxx_axisvalue,body_values.yyy_axisvalue
            body_values.attack_clicked = True
            body_values.fire_list.append((body_values.xxx_axisvalue+70,body_values.yyy_axisvalue+65,body_values.last_press))

            timer.attack_timer = time.time()
            mainplayer_body.display_background(self.display)
            attack.draw(self.display)




        else:


            if (time.time()-timer.attack_timer)>1/2.8:

                if (body_values.attack_clicked):
                    body_values.attack_clicked = False


            if (time.time()-timer.attack_timer)<1/2.8:


                mainplayer_body.display_background(self.display)
                attack.draw(self.display)
                attack.update()


            elif body_values.jumped:

                if mainplayer_body.up_floorChecking():
                    body_values.jumped = False

                else:

                    if (body_values.jumped):
                        mainplayer_body.coins_remover()
                        body_values.floor_click = True
                        if body_values.jumping_movevalue!= body_values.yyy_axisvalue:
                            mainplayer_body.yyy_upmover(self.display)
                            body_values.yyy_axisvalue -= 20


                        else:
                            body_values.jumped = False

            else:

                mainplayer_body.floor_standing()


                if body_values.yyy_axisvalue!=570:
                    mainplayer_body.coins_remover()
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
                    body_values.downed = False
                    body_values.downing_attack_count = False


    def mainloop(self):
        mainplayer_body.display_background(self.display)
        self.display.blit(pygame.image.load(images.rrun[7]),(body_values.xxx_axisvalue,body_values.yyy_axisvalue)) # game start standing___

        while True:
            pygame.time.delay(10)

            self.events()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()



            self.display.blit(pygame.image.load('S:/Mage/enemy.png'),(500,400))
            mainplayer_body.coins(self.display)
            mainplayer_body.fire(self.display)
            self.display.blit(images.coin_image,(1130,20)) #
            self.display.blit(body_values.font.render(str(body_values.coin_score),False,(255, 102, 0)),(1160,20))
            mainplayer_body.small_tiles(self.display,450,260)
            mainplayer_body.small_tiles(self.display, 550, 160)
            mainplayer_body.tile(self.display,200,570-110)
            mainplayer_body.tile(self.display,800,570-110)
            mainplayer_body.tile(self.display,1012,200)
            mainplayer_body.ground(self.display)
            pygame.display.flip()

player = main_window(1200,700,'RoguexWar')

if __name__ == "__main__":
    player.mainloop()