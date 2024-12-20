import cv2 as cv
import numpy as np

img=cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

#masking helps us to focus on specific parts of the image that we'd like to focus on
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked_image)

cv.waitKey(0)