#smoothing and various blurring techniques
import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

#blurring used to remove noise in the image

#averaging - defining a kernel window that computes the middle pixel intensity as the avergae of the surrounding intensities
average = cv.blur(img, (3,3))  #image and kernel size
cv.imshow('Average', average)

#gaussian blur - weighted average from surrounding pixels
gauss = cv.GaussianBlur(img, (7,7), 0) #0-std dev
cv.imshow('Gaussian', gauss)

#median Blur - median instead of average
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#bilateral blur - most effective - applies blurring but retains the adges in the image
bilateral = cv.bilateralFilter(img, 5, 15, 15)
#image, diameter, sigma color - number of colors in the neighborhood that will be considered, sigmaspace - if larger value, a wider range is considered
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)