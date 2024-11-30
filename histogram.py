import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#histograms allow to visualize the distribution of pixels in an image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) #pass everything as a list

plt.figure()
plt.title('Gray Hist')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#can also create a mask and compute a histogram for only that mask in the image
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray,mask=circle)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256]) #mask parameter set with mask we created

plt.figure()
plt.title('Gray Hist with mask')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0.256])
plt.show()

#Colour Histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
    plt.title('Color Hist')

plt.show()

cv.waitkey(0)