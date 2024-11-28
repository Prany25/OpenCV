import cv2 as cv

#reading an image
img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)

#reading a video
capture = cv.VideoCapture('videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)