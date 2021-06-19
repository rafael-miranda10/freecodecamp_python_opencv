import cv2 as cv

def changeRes(width, height):
    #Live video
    capture.set(3,width)
    capture.set(4, height)

def rescaleFrame(frame, scale=0.75):
    #Images, Videos and Live Videos
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0] * scale)
    dimensions = (width, height)
    return  cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('photos/2.jpg')
cv.imshow('Image', img)
resized_image = rescaleFrame(img)
cv.imshow('Resized Image', resized_image)
cv.waitKey(0)

#Reading Videos
capture = cv.VideoCapture('videos/1.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #exibe o video enquanto não pressionar a letra d
        break

capture.release()
cv.destroyAllWindows()