import pygame

class  snake:


    def __init__(self):
        self.display  = pygame.display.set_mode((1000,500))
        self.snakelist = []
        self.x_move = 10
        self.y_move = 10
        self.dead = []
        self.last_key = 'Right'
    def mainloop(self):


        def background():
            self.display.blit(pygame.image.load(r'C:\Users\mahen\Downloads\craftpix-516661-free-cartoon-forest-game-backgrounds\PNG\Cartoon_Forest_BG_04\Layers\Sky.png'),(0,0))



        while True:
            background()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type==pygame.KEYDOWN:

                    if (event.key==pygame.K_RIGHT):



                        self.last_key = "Right"

                        self.x_move+=10



                        self.snakelist.append((self.x_move,self.y_move))


                    elif (event.key==pygame.K_LEFT):
                        self.last_key= "Left"
                        self.x_move -= 10
                        self.snakelist.append((self.x_move, self.y_move))


                    elif (event.key==pygame.K_UP):
                        self.last_key = "Up"
                        self.y_move-=10
                        self.snakelist.append((self.x_move, self.y_move))

                    elif (event.key)==pygame.K_DOWN:
                        self.last_key = "Down"
                        self.y_move+=10
                        self.snakelist.append((self.x_move, self.y_move))



            if (self.last_key=='Right'):
                self.x_move+=10


                self.snakelist.append((self.x_move, self.y_move))


            elif (self.last_key=='Left'):
                self.x_move-=10


                self.snakelist.append((self.x_move, self.y_move))

            elif (self.last_key=='Up'):


                self.y_move-=10


                self.snakelist.append((self.x_move, self.y_move))


            elif (self.last_key=='Down'):
                self.y_move+=10
                self.snakelist.append((self.x_move, self.y_move))




            for (x,y) in self.snakelist[::-1]:




                if (x,y) in self.dead :
                    exit()

                self.dead.append((x, y))

                if (len(self.snakelist)>20):
                    del self.snakelist[0:1]
                    background()
                pygame.draw.rect(self.display, color='red', rect=[x,y, 20, 20])

            else:
                self.dead = []

            pygame.display.update()
snakee = snake();
snakee.mainloop()