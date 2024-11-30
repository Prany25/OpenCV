import cv2 as cv
import numpy as np

img = cv.imread('photos/boston.jpg')

cv.imshow('Boston', img)

#translating images
def translate(img, x, y):       #x and y are the number of pixels you want to shift in x and y axis
    transMat = np.float32([[1,0,x],[0,1,y]])     #translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# if x negative, shift to left
# -y up
# x right
# y down

translated = translate(img, -100, 100)
cv.imshow('translated', translated)

#rotation
def rotate(img, angle, rotationpoint=None):
    (height,width) = img.shape[:2]

    if rotationpoint is None:
        rotationpoint = (width//2,height//2)

        rotationmatrix = cv.getRotationMatrix2D(rotationpoint, angle, 1.0)
        dimensions = (width,height)

        return cv.warpAffine(img, rotationmatrix, dimensions)
    
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#flipping
flipped = cv.flip(img, 0)  #0 - vertical, 1 - horizontal, -1 - both
cv.imshow('Flipped', flipped)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)