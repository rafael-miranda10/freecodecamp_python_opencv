import cv2 as cv

img = cv.imread('photos/4.jpg')
cv.imshow('Image', img)

# converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
#cannyBlur = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
#cv.imshow('Canny Edges Blur', cannyBlur)


# dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

# resize

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# croping
croped = img[50:200, 200:400]
cv.imshow('Croped', croped)

cv.waitKey(0)

