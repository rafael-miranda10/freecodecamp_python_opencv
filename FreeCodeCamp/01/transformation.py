import cv2 as cv
import numpy as np

img = cv.imread('photos/4.jpg')
cv.imshow('Image', img)

# Trasnlation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


#  - X  --> Left
#  - Y  --> Up
#  x --> Rigth
#  x --> Down

translated = translate(img, -100 , 100)
#cv.imshow('Translated', translated)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
#cv.imshow('Roteted', rotated)

#rotated_rotated = rotate(rotated, -45)
rotated_rotated = rotate(img, -90)
#cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

# Flipping
#flip = cv.flip(img, 0)
#flip = cv.flip(img, 1)
flip = cv.flip(img, -1)
#cv.imshow('Flip', flip)

# Cropping
croped = img[200:400, 300:400]
cv.imshow('Croped', croped)

cv.waitKey(0)

#Parei no minuto 57:00