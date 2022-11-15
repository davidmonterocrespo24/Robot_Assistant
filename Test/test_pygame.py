# Simple pygame program
import multiprocessing 
# Import and initialize the pygame library
import pygame
import time
import os
import pygame
import glob
 
SIZE = WIDTH, HEIGHT = 150, 200 #the width and height of our screen
FPS = 20 #Frames per second

f_imagenes = os.listdir('D:\David\Python\Ewon\Eye images')
imagenes=[]

for i in range(0,len(f_imagenes)):
    imagenes.append(pygame.image.load('D:\David\Python\Ewon\Eye images\\'+f_imagenes[i]))



def display(images):
    for i in images:
       win.blit(imagenes[i], (0,0))


def sad():
    #set_angles(lf=lfmax, lt=ltmin, rf=rfmin, rt=rtmax, nk=nkmax)
    p = multiprocessing.Process(target=display, args=([13,14,15,16], ))
    p.start()
    time.sleep(1)

def happy():
    print("animation: happy")
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax/2, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax/2, nk=nkmin) 
    p = multiprocessing.Process(target=display, args=([0,1,2,3,4,5,6], ))
    p.start()
    #for i in range(0,2):
    #    set_angles(lf=lfmin, lt=ltmax/2, rf=rfmax, rt=rtmax/2, nk=nkst)
    #    time.sleep(0.5)
    #    set_angles(lf=lfmax, lt=ltmax/2, rf=rfmin, rt=rtmax/2, nk=nkst)
    #    time.sleep(0.5)
    time.sleep(1)
    
def angry():
    print("animation: angry")
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=(ltmax/4)*3, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax/4, nk=nkmin) 
    p = multiprocessing.Process(target=display, args=([7,8,9,10,11,12], ))
    p.start()
    time.sleep(1)
   
def listen():
    print("animation: listen")
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst)
    p = multiprocessing.Process(target=display, args=([13,14,15,16,17,18,19], ))
    p.start()
    time.sleep(1)
    
def random1():
    #set_angles(lf=lfmax, lt=ltmin, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst)
    p = multiprocessing.Process(target=display, args=([5,4,3,2,1,0], ))
    p.start()
    time.sleep(1)
    
def random2():
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin, rt=rtmax, nk = nkst)
    p = multiprocessing.Process(target=display, args=([5,4,3,2,1,0], ))
    p.start()
    time.sleep(1)

def default():
    print("animation: default")
    p = multiprocessing.Process(target=display, args=([0,1,2,3,4,5], ))
    p.start()
    #for i in range(0,2):
    #    set_angles(lf=lfmin, lt=ltmax, rf=rfmin, rt=rtmin, nk=nkst)
    #    time.sleep(0.5)
     #   set_angles(lf=lfmax, lt=ltmax, rf=rfmax, rt=rtmin, nk=nkst)
    #    time.sleep(0.5)

def random4():
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax, nk = nkst)
    p = multiprocessing.Process(target=display, args=([5,4,3,2,1,0], ))
    p.start()
    time.sleep(1)
    
def random5():
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmin, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst)
    p = multiprocessing.Process(target=display, args=([5,4,3,2,1,0], ))
    p.start()
    time.sleep(1)
    
    
def zero():
    angry()


def fear():
    print("animation: fear")
    angry()

def disgust():
    print("animation: disgust")
    angry()

def surprise():
    print("animation: surprise")
    angry()

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = [pygame.image.load(img) for img in glob.glob("images\\*.png")]
        self.index = 0
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1


pygame.init()




# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    catImg = pygame.image.load('D:\David\Python\Robot\R11E.png')
    catx = 10
    caty = 10

    happy()


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()