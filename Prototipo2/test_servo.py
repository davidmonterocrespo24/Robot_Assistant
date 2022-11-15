import multiprocessing 
from adafruit_servokit import ServoKit
import time


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



def init():
    global ser    
    global kit
    kit = ServoKit(channels=16)
    global startAngles
    

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
    set_angles(lf=lfmax, lt=ltmin, rf=rfmin, rt=rtmax, nk=nkmax)
    time.sleep(1)

def happy():
    print("animation: happy")
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax/2, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax/2, nk=nkmin)     
    for i in range(0,2):
        set_angles(lf=lfmin, lt=ltmax/2, rf=rfmax, rt=rtmax/2, nk=nkst)
        time.sleep(0.5)
        set_angles(lf=lfmax, lt=ltmax/2, rf=rfmin, rt=rtmax/2, nk=nkst)
        time.sleep(0.5)
    time.sleep(1)
    
def angry():
    print("animation: angry")
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=(ltmax/4)*3, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax/4, nk=nkmin)     
    time.sleep(1)
   
def listen():
    print("animation: listen")
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst) 
    time.sleep(0.5)
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmin, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax, nk = nkst)    
    time.sleep(1)
    
def random1():
    set_angles(lf=lfmax, lt=ltmin, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst)    
    time.sleep(1)
    
def random2():
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin, rt=rtmax, nk = nkst)   
    time.sleep(1)

def default():
    print("animation: default")    
    for i in range(0,2):
        set_angles(lf=lfmin, lt=ltmax, rf=rfmin, rt=rtmin, nk=nkst)
        time.sleep(0.5)
        set_angles(lf=lfmax, lt=ltmax, rf=rfmax, rt=rtmin, nk=nkst)
        time.sleep(0.5)

def random4():
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmax, rf=rfmin + (rfmax-rfmin)/2, rt=rtmax, nk = nkst)   
    time.sleep(1)
    
def random5():
    set_angles(lf=lfmin + (lfmax-lfmin)/2, lt=ltmin, rf=rfmin + (rfmax-rfmin)/2, rt=rtmin, nk = nkst)   
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

init()
happy()
time.sleep(3)
angry()
time.sleep(3)
print("LISTEN+++++++++++++++++++++++++++++")
listen()
time.sleep(3)
print("SAD+++++++++++++++++++++++++++++")
sad()
time.sleep(3)
print("HAPPY+++++++++++++++++++++++++++++")
fear()
time.sleep(3)
print("DISGUST+++++++++++++++++++++++++++++")
disgust()
time.sleep(3)
print("SURPRISE+++++++++++++++++++++++++++++")
surprise()
time.sleep(3)
print("Defaul+++++++++++++++++++++++++++++")
default()
time.sleep(3)
print("Random1+++++++++++++++++++++++++++++")
random1()
time.sleep(3)
print("Random2+++++++++++++++++++++++++++++")
random2()
time.sleep(3)
print("Random4+++++++++++++++++++++++++++++")
random4()
time.sleep(3)
print("Random5+++++++++++++++++++++++++++++")
random5()
time.sleep(3)
print("ZERO+++++++++++++++++++++++++++++")
zero()



