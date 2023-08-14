import cv2 as cv

#Reading an image

img = cv.imread('images/cat-3.jpg')
cv.imshow('Cat-3', img)
cv.waitKey(0)


#Reading a video

capture = cv.VideoCapture('videos/dog-360p.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Dog.mp4',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
