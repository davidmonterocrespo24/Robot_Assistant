import time
import math
import multiprocessing 
from adafruit_servokit import ServoKit
import serial
import sys
import os
import re

e = "\xff\xff\xff"

LF = 4 #left flap
LT = 5 # 
RT = 6 #right turn
RF = 7 #right flap
NK = 8 #neck

lfmin = 90
lfmax = 160
ltmin = 0
ltmax = 140
rtmin = 0
rtmax = 140
rfmin = 80
rfmax = 150
nkmin = 20
nkmax = 100
nkst = 40


startAngles = {
    LF:lfmin + (lfmax-lfmin)/2,
    RF:rfmin + (rfmax-rfmin)/2,
    LT:ltmax,
    RT:rtmin,
    NK:nkst 
    }



def setDownloadBaudrate(ser, baudrate):
    return True
     

def init():
    global ser
    #setDownloadBaudrate(ser, 9600)
    
    global kit

    global startAngles
    

def display(images):
    for i in images:
        ser.write(b"p0.pic=")
        ser.write(bytes(str(i), 'utf-8'))
        ser.write(b"\xff\xff\xff")
        time.sleep(0.1)

def kit_angle(servoNum, angle, sleepTime):
    kit.servo[servoNum].angle = angle
    
def set_angles(lf=-1, lt=-1, rf=-1, rt=-1, nk=-1):
    if lf >= lfmin and lf <= lfmax:
        p1 = multiprocessing.Process(target=kit_angle, args=(LF,lf, 0., ))
    if rf >= rfmin and rf <= rfmax:
        p2 = multiprocessing.Process(target=kit_angle, args=(RF,rf, 0, ))
        
    if lt >= ltmin and lt <= ltmax:
        p3 = multiprocessing.Process(target=kit_angle, args=(LT,lt,0, ))
    if rt >= rtmin and rt <= rtmax:
        p4 = multiprocessing.Process(target=kit_angle, args=(RT,rt,0, ))
    if nk >= nkmin and nk<=nkmax:    
        p5 = multiprocessing.Process(target=kit_angle, args=(NK,nk,0, ))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    
    
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
    for i in range(0,2):
        set_angles(lf=lfmin, lt=ltmax/2, rf=rfmax, rt=rtmax/2, nk=nkst)
        time.sleep(0.5)
        set_angles(lf=lfmax, lt=ltmax/2, rf=rfmin, rt=rtmax/2, nk=nkst)
        time.sleep(0.5)
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
    for i in range(0,2):
        #set_angles(lf=lfmin, lt=ltmax, rf=rfmin, rt=rtmin, nk=nkst)
        time.sleep(0.5)
        #set_angles(lf=lfmax, lt=ltmax, rf=rfmax, rt=rtmin, nk=nkst)
        time.sleep(0.5)

def random4():
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax, nk = nkst)
    p = multiprocessing.Process(target=display, args=([5,4,3,2,1,0], ))
    p.start()
    time.sleep(1)
    
def random5():
    #set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmin, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst)
    p = multiprocessing.Process(target=display, args=([5,4,3,2,1,0], ))
    p.start()
    time.sleep(1)
    

def mover_orejas_derecha_izquierda():
    p = multiprocessing.Process(target=display, args=([0,1,2,3,4,5], ))
    p.start()
    for i in range(0,2):
        #set_angles(lf=lfmin, lt=ltmax, rf=rfmin, rt=rtmin, nk=nkst)
        time.sleep(0.5)
        #set_angles(lf=lfmax, lt=ltmax, rf=rfmax, rt=rtmin, nk=nkst)
        time.sleep(0.5)

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



