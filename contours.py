import cv2 as cv

img = cv.imread('photos/cats.jpg')

cv.imshow('Cats', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
 

cv.waitKey(0)