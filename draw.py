import cv2 as cv
import numpy as np

#blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

blank[:]=0,255,0 #green
cv.imshow('Green', blank)

#only coloured for a specific range
blank[200:300, 300:400] = 0,0,255 #red
cv.imshow('Red', blank)

#draw a line over the image
cv.line(blank, (0,0), (250,270), (255,255,255), thickness=2)
cv.imshow('Line', blank)

#draw rectangle over an image
cv.rectangle(blank, (0,0), (250,270), (0,255,0), thickness=cv.FILLED)   #start, end, colour, thickness
cv.imshow('Rectangle', blank)

#draw circle over image
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)   #centre, radius, colour thickness
cv.imshow('Circle', blank)

#writing text on the image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #image, text, font, fontscale, colour, thickness
cv.imshow('Text', blank)

cv.waitKey(0)