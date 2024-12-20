import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200),200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND - intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('AND', bitwise_and)

#bitwise OR - non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow('OR', bitwise_or)

#bitwise XOR - non-intersecting regions
bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow('XOR', bitwise_xor)

#bitwise NOT - inverts the color
bitwise_not = cv.bitwise_not(circle)
cv.imshow('NOT', bitwise_not)

cv.waitKey(0)