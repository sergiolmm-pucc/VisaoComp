import numpy as np
import cv2
import requests
import grequests
import time

async_list = []

# http://192.168.15.43/on?R=95
# http://192.168.15.43/on?L=95
def ligaR(potencia):
   resp = ('http://192.168.15.74/on?R='+potencia)
   return resp
def ligaL(potencia):
   resp = ('http://192.168.15.74/on?L='+potencia)
   return resp
def pararR():
   resp = ('http://192.168.15.74/on?R=95')
   return resp
def pararL():
   resp = ('http://192.168.15.74/on?L=95')
   return resp

def mandarRequest(req):
    action_item = grequests.get(req)
    # Add the task to our list of things to do via async
    async_list.append(action_item)
    grequests.map(async_list,gtimeout=0.2)
    async_list.clear()



cap = cv2.VideoCapture("http://192.168.15.74:81")
print("Iniciando...")
while(True):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Passo 2: Blur/Suavização da imagem
    suave = cv2.blur(img, (7, 7))
    temp = np.vstack([
         np.hstack([img, suave ]) ])
    cv2.imshow('frame',temp)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('y'):
        break
    if key == ord('w'):
        cv2.imwrite("saida.jpg", temp)
    try:        
        if key == ord('a'): 
            print('a-> '+ ligaL('60'))       
            mandarRequest(ligaL('60'))
        if key == ord('s'):    
            print('s-> '+ ligaR('60'))       
            mandarRequest(ligaR('60'))
        if key == ord('q'): 
            print('q-> '+ ligaL('120'))       
            mandarRequest(ligaL('120'))
        if key == ord('w'):    
            print('w-> '+ ligaR('120'))       
            mandarRequest(ligaR('120'))
        if key == ord('z'):        
            print('Parando')   
            mandarRequest(pararL())
            #mandarRequest(pararR())
           # time.sleep(0.3)
        if key == ord('x'):        
            print('Parando')   
            #mandarRequest(pararL())
            mandarRequest(pararR())            
           # time.sleep(0.3)
    except requests.exceptions.Timeout:
        print("timeout")

cap.release()
cv2.destroyAllWindows()