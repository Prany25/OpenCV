import cv2 as cv

#suitable for images, videos and live vids
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos/puppy.mp4')

#suitable only for live videos
def ChangeResolution(width, height):
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue, frame = capture.read()

    frame_resized =  rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
