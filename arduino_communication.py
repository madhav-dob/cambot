import cv2
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)


#______arduino part_______
from pyfirmata import Arduino , util

from time import sleep

from pyfirmata.pyfirmata import SERVO


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(2)


board = Arduino('COM3')
pin = 10
board.digital[pin].mode=SERVO

def rotate_servo(pin, angle):
    board.digital[pin].write(angle)
    time.sleep(0.0015)
    #sleep(0.0005)



#______main progarm_________
pos = 85
rotate_servo(pin, pos)
buffer = False
buffer_no = 0
print("Start ! ")
while True:
    _ , img = cap.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY )

    faces = face_cascade.detectMultiScale(img , 1.3 , 6, minSize= [80,80])
    if len(faces)>0:
        [ z, y, w ,h] =  faces[0]
        #print(z,'    ', y ,'    ', w,'      ', h)
        cv2.rectangle(img, (z,y), (z+w , y+h) , (0 , 228, 0), 3)
        x = (z+w)/2
        #print(x)


        if x <180  :
            #print("position: ",x, "servo : ",pos)
            if pos<170:
                rotate_servo(pin, pos+1)
                pos += 1

                x_axis = 'rightwards'
            else:
                x_axis = 'max limit of rotation'
        elif x  > 215 :
            #print("position: ",x, "servo : ",pos)
            if pos>10:
                rotate_servo(pin, pos-1)
                pos -= 1
                x_axis = 'leftwards'
            else:
                x_axis = 'max limit of rotation'

        else :
             #print("else mein hu")
             #print("position: ",x, "servo : ",pos)
             x_axis = 'stop'

                 #time.sleep(0.5)

        #print (x_axis )





    cv2.imshow('img' , img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()