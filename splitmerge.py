import cv2 as cv
import numpy as np

img = cv.imread('photos/boston.jpg')
cv.imshow('Boston', img)

#splitting an image into its respective color channels - blue, green and red
b,g,r = cv.split(img)

#shows the intensity of each color as light and dark in the form of a grayscale image
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape) #3 in the shape represents 3 color channels
print(b.shape)
print(g.shape)
print(r.shape)

#merging the color channels together
merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)

#to see the actual color involved instead of grayscale
#by reconstructing the image
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
 
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)