import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(2)


while True:
    _ , img = cap.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY )

    faces = face_cascade.detectMultiScale(img , 1.1 , 4)
    if len(faces)>0:
        [ x, y, w ,h] =  faces[0]
        print(x,'    ', y ,'    ', w,'      ', h)
        cv2.rectangle(img, (x,y), (x+w , y+h) , (0 , 228, 0), 3)

        if x > 235  :
            x_axis = 'rightwards'
        elif x  < 220 :
            x_axis = 'leftwards'

        else :
            x_axis = 'stop'

        if y < 110 :
            y_axis = 'upwards'

        elif y > 125 :
            y_axis = 'downwards'

        else :
            y_axis = 'stop'
        
        #print (x_axis , y_axis)




    cv2.imshow('img' , img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()