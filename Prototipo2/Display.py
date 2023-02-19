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
import multiprocessing 
import time

SIZE = WIDTH, HEIGHT = 400, 200 #the width and height of our screen
FPS = 5 #Frames per second
 


 
class MySprite(pygame.sprite.Sprite):
    
    expression_index={}
    LF = 5 #oreja_izquieda
    LT = 4 #movimiento izquierdo
    RT = 7 #movimiento derecho
    RF = 6 #oreja_derecha
    NK = 8 #neck

    lfmin = 35
    lfmax = 115
    ltmin = 0#*
    ltmax = 80

    rfmin = 0
    rfmax = 80
    rtmin = 80
    rtmax = 0#*


    nkmin = 0
    nkmax = 60
    nkst = 20


    startAngles = {
        LF:lfmin,
        RF:rfmin,
        LT:ltmin,
        RT:rtmin,
        NK:nkst 
        }

    def __init__(self):
        super(MySprite, self).__init__()
        f_imagenes=[]
        expression= ['Enojado','Normal','Muerto','Asustado','Feliz','Triste','Sorprendido','Guino','Really','Amor','Disparar']       
        self.images=[]
        index=0
        for i in range(0,len(expression)):
            archivos=os.listdir(os.path.join(os.getcwd(),'Eyes',expression[i]))
            #print("Cargando archivos..............:"+str(os.path.join(os.getcwd(),'Eyes',expression[i])))   
            arch=[]      
            for k in range(0,len(archivos)):
                arch.append(str(k+1)+expression[i]+".png")     
                print("Cargando archivos..............:"+str(str(k+1)+expression[i]))
            f_imagenes.append(arch)
            index_array=[]            
            for j in range(0,len(f_imagenes[i])):
                index_array.append(index)
                index=index+1
                ima=os.path.join(os.path.join(os.getcwd(),'Eyes',expression[i],f_imagenes[i][j]))
                self.images.append(pygame.transform.scale(pygame.image.load(ima),(480, 320)))             
            self.expression_index.update({expression[i]:index_array})
        self.index = 0
        self.state='Normal'
        self.rect = pygame.Rect(5, 5, 150, 198)
        print(self.expression_index)
        self.init()

    def update(self,):              
        self.animation(self.expression_index[self.state] )
        
    def set_state(self,state):
        self.state=state
       
        print("Estado:------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", state)
        if self.state == 'Enojado':
            self.angry()
        elif self.state == 'Feliz':
            self.happy()
        elif self.state == 'Triste':
            self.sad()
        elif self.state == 'Asustado':
            self.random1()
        elif self.state == 'Sorprendido':
            self.random2()
        elif self.state == 'Guino':
            self.default()
        elif self.state == 'Normal':
            self.random4()
        elif self.state == 'Muerto':
            self.random5()
        elif self.state == 'Really':
            self.random2()
        elif self.state == 'Amor':
            self.mover_orejas_derecha_izquierda()
        elif self.state == 'Disparar':
            self.disparar()
        

    def animation(self,index_image):
        if self.index >= index_image[len(index_image)-1]:
            self.index = index_image[len(index_image)-1]
        if self.index < index_image[0]:
            self.index = index_image[0]               
        self.image = self.images[self.index]
        self.index += 1
    

    def init(self):
        global ser    
        global startAngles
        

    def kit_angle(self,servoNum, angle, sleepTime):
        print("Servo: ",servoNum," Angle: ",angle," Sleep: ",sleepTime)
        
    def set_angles(self,lf=-1, lt=-1, rf=-1, rt=-1, nk=-1): 
        p1=False
        p2=False
        p3=False
        p4=False
        p5=False   
        if lf >= self.lfmin and lf <= self.lfmax:
            p1 = multiprocessing.Process(target=self.kit_angle, args=(self.LF,lf, 0., ))
        if rf >= self.rfmin and rf <= self.rfmax:
            p2 = multiprocessing.Process(target=self.kit_angle, args=(self.RF,rf, 0, ))
        if lt >= self.ltmin and lt <= self.ltmax:
            p3 = multiprocessing.Process(target=self.kit_angle, args=(self.LT,lt,0, ))
        if rt >= self.rtmin and rt <= self.rtmax:
            p4 = multiprocessing.Process(target=self.kit_angle, args=(self.RT,rt,0, ))
        if nk >= self.nkmin and nk<=self.nkmax:    
            p5 = multiprocessing.Process(target=self.kit_angle, args=(self.NK,nk,0, ))
    
       
    def sad(self):
        self.set_angles(lf=self.lfmax, lt=self.ltmin, rf=self.rfmin, rt=self.rtmax, nk=self.nkmax)
        time.sleep(1)

    def happy(self):
        print("animation: happy")
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmax/2, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmax/2, nk=self.nkmin)     
        for i in range(0,2):
            self.set_angles(lf=self.lfmin, lt=self.ltmax/2, rf=self.rfmax, rt=self.rtmax/2, nk=self.nkst)
            time.sleep(0.5)
            self.set_angles(lf=self.lfmax, lt=self.ltmax/2, rf=self.rfmin, rt=self.rtmax/2, nk=self.nkst)
            time.sleep(0.5)
        time.sleep(1)
        
    def angry(self):
        print("animation: angry")
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=(self.ltmax/4)*3, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmax/4, nk=self.nkmin)     
        time.sleep(1)
    
    def listen(self):
        print("animation: listen")
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmax, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmin, nk = self.nkst) 
        time.sleep(0.5)
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmin, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmax, nk = self.nkst)    
        time.sleep(1)
        
    def random1(self):
        self.set_angles(lf=self.lfmax, lt=self.ltmin, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmin, nk = self.nkst)    
        time.sleep(1)
        
    def random2(self):
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmax, rf=self.rfmin, rt=self.rtmax, nk = self.nkst)   
        time.sleep(1)

    def default(self):
        print("animation: default")    
        for i in range(0,2):
            self.set_angles(lf=self.lfmin, lt=self.ltmax/2, rf=self.rfmin, rt=self.rtmin, nk=self.nkst)
            time.sleep(0.5)
            self.set_angles(lf=self.lfmax, lt=self.ltmin, rf=self.rfmax, rt=self.rtmax/2, nk=self.nkst)
            time.sleep(0.5)

    def random4(self):
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmax, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmax, nk = self.nkst)   
        time.sleep(1)
        
    def random5(self):
        self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmin, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmin, nk = self.nkst)   
        time.sleep(1)
        
        
    def zero(self):
        self.angry()

    def fear(self):
        print("animation: fear")
        self.angry()

    def disgust(self):
        print("animation: disgust")
        self.angry()

    def surprise(self):
        print("animation: surprise")
        self.angry()

    def mover_orejas_derecha_izquierda(self):
        print("animation: default")    
        for i in range(0,2):
            self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmax, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmax, nk = self.nkst)  
            time.sleep(0.5)            
            self.set_angles(lf=self.lfmin + (self.lfmax-self.lfmin)/2, lt=self.ltmin, rf=self.rfmin + (self.rfmax-self.rfmin)/2, rt=self.rtmin, nk = self.nkst)  
            time.sleep(0.5)

    def disparar(self):
        print("animation: default")    
        for i in range(0,2):
            self.set_angles(lf=self.lfmax, lt=self.ltmin, rf=self.rfmax , rt=self.rtmin, nk = self.nkst)  
            time.sleep(0.5)            
            self.set_angles(lf=self.lfmax, lt=self.ltmin+(self.ltmax-self.lfmin)/2, rf=self.rfmax , rt=self.rtmin+(self.rtmax-self.rfmin)/2, nk = self.nkst)   
            time.sleep(0.5)