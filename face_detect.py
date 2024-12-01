import cv2 as cv

img = cv.imread('photos/girl.jpg')
cv.imshow('Girl', img)

#convert to grayscale first
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) #returns as a list
print("Number of people detected: ", len(faces_rect)) #number of faces detected

#drawing rectangles over faces

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', img)

#can adjust scale factor and minNeighbors to reduce noise detection
 

cv.waitKey(0)