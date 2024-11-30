import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')

cv.imshow('Cats', img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

#grayscale
gray = cv.cvtColor(img,  cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow('Edges',   canny)

ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', threshold)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#contours - list of all contours 
#hierarchies - representation of all the contours
  
print(len(contours)) #no. of contours

cv.drawContours(blank, contours, -1, (0,0,255), 2)
#displaying the contours on a blank image, since we want to print
#all the contours, we use -1, 2 is the thickness
cv.imshow('Contours Drawing', blank)
cv.waitKey(0)