import cv2 as cv

img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #image, kernels should always be odd, border
cv.imshow('Blur', blur)                               #increase kernel size to increase blur

#end cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
#if want to reduce edges, apply blur then cascade

#dilate an image
dilated = cv.dilate(canny, (7,7), iterations=3) #image, kernel size, iterations
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations =1) #reversing dilations
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #resizes to given size ignoring the aspect ratio
cv.imshow('resized', resized)

#cropping
cropped = img[50:200, 200:400] #giving the coordinates for the area we need to be cropped
cv.imshow('cropped', cropped)

cv.waitKey(0)