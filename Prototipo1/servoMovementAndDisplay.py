from ast import Expression
from re import S
from traceback import print_tb
import pygame
import glob
import os
import time
from glob import glob
import sys
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 400, 200 #the width and height of our screen
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