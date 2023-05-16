import glob
import random
import sys, pygame,itertools,time

pygame.display.set_caption('Platform')

class Game(pygame.sprite.Sprite):

    def __init__(self, width, height):
        self.width = width
        self.height = height


        self.window = pygame.display.set_mode((width,height))
        self.standB_Value = (620-85)

        self.xxx = 50
        self.yyy = self.standB_Value

        self.clock = pygame.time.Clock()


    def mainloop(self):



        while True:
            pygame.time.delay(80)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            group.draw(self.window)
            pygame.display.flip()
            self.clock.tick(60)



class dont(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('S:/Mage/mage.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [300,500]




game = Game(*(1200,650))

do = dont()
group = pygame.sprite.Group()
group.add(do)


if __name__ == '__main__':
    game.mainloop()







