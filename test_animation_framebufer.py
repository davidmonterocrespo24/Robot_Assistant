from re import S
import pygame
import glob
import os
import os
import time
import random


class pyscope :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        my_sprite = MySprite()
        my_group = pygame.sprite.Group(my_sprite)
        clock = pygame.time.Clock()
        loop = 1
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = 0
                if event.type == KEYDOWN:
                # Change the keyboard variables.
                    if event.key == K_LEFT or event.key == K_a:
                        my_sprite.index=0
                        my_sprite.set_state('Blink')
                    if event.key == K_RIGHT or event.key == K_d:
                        my_sprite.index=0
                        my_sprite.set_state('Surprised')
                    if event.key == K_UP or event.key == K_w:
                        my_sprite.index=0
                        my_sprite.set_state('Happy')
                    if event.key == K_DOWN or event.key == K_s:
                        my_sprite.index=0
                        my_sprite.set_state('Wink')
        pygame.quit()      
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

SIZE = WIDTH, HEIGHT = 480, 320 #the width and height of our screen
FPS = 5 #Frames per second
 

class MySprite(pygame.sprite.Sprite):
    
    expression_index={}

    def __init__(self):
        super(MySprite, self).__init__()
        f_imagenes=[]
        expression= ['Angry','Blink','Dead','Fear','Happy','Sad','Surprised','Wink','Really']       
        self.images=[]
        index=0
        for i in range(0,len(expression)):
            print("+++++++"+str(os.listdir(os.path.join(os.getcwd(),'Eyes',expression[i]))))
            f_imagenes.append(os.listdir(os.path.join(os.getcwd(),'Eyes',expression[i])))
            index_array=[]            
            for j in range(0,len(f_imagenes[i])):
                index_array.append(index)
                index=index+1
                ima=os.path.join(os.path.join(os.getcwd(),'Eyes',expression[i],f_imagenes[i][j]))
                self.images.append(pygame.image.load(ima))             
            self.expression_index.update({expression[i]:index_array})
        self.index = 0
        self.state='Blink'
        self.rect = pygame.Rect(5, 5, 150, 198)
        print(self.expression_index)

    def update(self,):              
        self.animation(self.expression_index[self.state] )
        
    def set_state(self,state):
        self.state=state

    def animation(self,index_image):
        if self.index >= index_image[len(index_image)-1]:
            self.index = index_image[len(index_image)-1]
        if self.index < index_image[0]:
            self.index = index_image[0]               
        self.image = self.images[self.index]
        self.index += 1

 
scope = pyscope()
scope.test()
time.sleep(10)