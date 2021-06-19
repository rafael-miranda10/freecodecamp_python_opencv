import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/4.jpg')
cv.imshow('Image', img)


# BGR to GrayScale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Sacle', gray)

# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()


# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# LAB to BGR (bad result)
lab_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', lab_bgr)


cv.waitKey(0)

