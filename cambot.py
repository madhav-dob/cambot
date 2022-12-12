#_____face detection part______
import cv2
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)


#______arduino part_______
from pyfirmata import Arduino , util

from time import sleep

from pyfirmata.pyfirmata import SERVO

board = Arduino('COM3')
pin = 10
board.digital[pin].mode=SERVO

def rotate_servo(pin, angle):
    board.digital[pin].write(angle)
    #time.sleep(0.0015)
    #sleep(0.0005)



#______main progarm_________
pos = 90
rotate_servo(pin, 90)
while True:
    _ , img = cap.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY )

    faces = face_cascade.detectMultiScale(img , 1.1 , 4)
    if len(faces) >0 :
        [ z, y, w ,h] = faces[0]
            #print(x,'    ', y ,'    ', w,'      ', h)
        cv2.rectangle(img, (z,y), (z+w , y+h) , (0 , 228, 0), 3)
        x = (z+w)/2
        if x <220  :
            print("position: ",x, "servo : ",pos)
            if pos<180:
                rotate_servo(pin, pos+1)
                pos += 1

                x_axis = 'rightwards'
            else:
                x_axis = 'max limit of rotation'
        elif x  > 235 :
            print("position: ",x, "servo : ",pos)
            if pos>0:
                rotate_servo(pin, pos-1)
                pos -= 1
                x_axis = 'leftwards'
            else:
                x_axis = 'max limit of rotation'

        else :
             print("else mein hu")
             print("position: ",x, "servo : ",pos)
             x_axis = 'stop'
             time.sleep(5)
            # if y < 110 :
            #     y_axis = 'upwards'

            # elif y > 125 :
            #     y_axis = 'downwards'

            # else :
            #     y_axis = 'stop'

            #print (x_axis , y_axis)
        print (x_axis )
    else:
        print("No faces detected")



#     cv2.imshow('img' , img)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#
# cap.release()