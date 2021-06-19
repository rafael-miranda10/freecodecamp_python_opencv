import cv2 as cv
import numpy as np

img = cv.imread('photos/4.jpg')
cv.imshow('Image', img)

# Averaging
average = cv.blur(img, (7,7)) #(3,3) (5,5)
cv.imshow('Average Blur', average)


#Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 30,25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)

#parei no minuto 1:44:25