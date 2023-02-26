import pygame
from Display import *
from emotions import *
from assistant_con_animation import Assistant

class Animation ():


    def __init__(self, startEmotion):       
        self.current_emotion = 0
        self.previous_emotion = 0
        pygame.init()
        screen = pygame.display.set_mode((480, 320))
        #pygame.display.set_caption("Trace")
        self.my_sprite = MySprite()
        self.my_group = pygame.sprite.Group(self.my_sprite)   
        #screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.assistant = Assistant(self,language_code="en-AU")
        self.assistant.start()


    def run(self):        
        global first
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
                self.current_emotion = self.current_emotion+1
            else:
                print("RUN------current_emotion----"+str(emotions[self.current_emotion][0])+"--------------"+str(emotions[self.previous_emotion][0])+"--previous_emotion------") 
                if self.current_emotion != self.previous_emotion:
                    print("Emociones------------------------------------"+emotions[self.previous_emotion][0])
                    self.previous_emotion = self.current_emotion
                    self.my_sprite.set_state(emotions[self.current_emotion][0])
        
            self.my_group.update()      
            self.screen.fill((0,0,0))
            self.my_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(15)
        self.assistant.stop()
        self.assistant.join()
        pygame.quit()
        quit()

