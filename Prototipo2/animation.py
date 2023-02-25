import pygame
from Display import *
from emotions import *
current_emotion = 0
previous_emotion = 0

class Animation ():


    def __init__(self, startEmotion):       
        current_emotion = startEmotion
        previous_emotion = startEmotion
        pygame.init()
        screen = pygame.display.set_mode((480, 320))
        #pygame.display.set_caption("Trace")
        self.my_sprite = MySprite()
        self.my_group = pygame.sprite.Group(self.my_sprite)   
        #screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        self.screen = screen
        self.clock = pygame.time.Clock()


    def run(self):        
        global first
        global current_emotion
        global previous_emotion
        loop = 1

        first = False
        while loop:
            for event in pygame.event.get():
                print("EVENTO------------------"+str(event.type)+"-----------------")
                print(event.type)
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE or event.type == pygame.K_LCTRL:
                    loop = 0
            if first:               
                first = False
                self.my_sprite.set_state('Normal')
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_emotion = current_emotion+1
            else:
                print("RUN------current_emotion----"+str(emotions[current_emotion][0])+"--------------"+str(emotions[previous_emotion][0])+"--previous_emotion------") 
                if current_emotion != previous_emotion:
                    print("Emociones------------------------------------"+emotions[previous_emotion][0])
                    previous_emotion = current_emotion
                    self.my_sprite.set_state(emotions[current_emotion][0])
        
            self.my_group.update()      
            self.screen.fill((0,0,0))
            self.my_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(15)
        pygame.quit()
        quit()

def set_emotion(str):
        splits = str.split()
        for split in splits:
                for i in range(len(emotions)):
                        for j in range(len(emotions[i])):
                                if split.upper() == emotions[i][j].upper():
                                        return i
        return 1
