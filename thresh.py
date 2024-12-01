import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

#thresholding - binarization of an image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
            #threshold is the value that we pass and thresh is the thresholded image
cv.imshow('Simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholded Inverse', thresh_inv)

#Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresh', adaptive_thresh)

cv.waitKey(0)