import pyfirmata
from tkinter import *
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)


# don't forget to change the serial port to suit
board = pyfirmata.Arduino('COM3')

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

# set up pin D9 as Servo Output
pin9 = board.get_pin('d:10:s')


def rotate_servo(a):
    pin9.write(a)


# ______main progarm_________
pos = 90
rotate_servo(90)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # print(x,'    ', y ,'    ', w,'      ', h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 228, 0), 3)

        if x < 220:
            print(pos)
            if pos < 270:
                rotate_servo(pos + 1)
                pos += 1
                x_axis = 'rightwards'
            else:
                x_axis = 'max limit of rotation'
        elif x > 235:
            print(pos)
            if pos > 90:
                rotate_servo(pos - 1)
                pos -= 1
                x_axis = 'leftwards'
            else:
                x_axis = 'max limit of rotation'

        else:
            x_axis = 'stop'

        # if y < 110 :
        #     y_axis = 'upwards'

        # elif y > 125 :
        #     y_axis = 'downwards'

        # else :
        #     y_axis = 'stop'

        # print (x_axis , y_axis)
        print(x_axis)

# set up GUI
# root = Tk()
#
# # draw a nice big slider for servo position
# scale = Scale(root,
#               command=move_servo,
#               to=175,
#               orient=HORIZONTAL,
#               length=400,
#               label='Angle')
# scale.pack(anchor=CENTER)
#
# # run Tk event loop
# root.mainloop()