import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('Cat', img)

#Step1: blurring the image to remove noise
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Step2: converting the image to grayscale
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Step3: finding the edges in the image using Canny edge detection
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny)

#step3 : another way of finding the edges in the iamge is by using thresholding
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded Image', thresh)

#Step4: finding the contours in the image
contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Number of contours found: {len(contours)}')

#step5: craeting a blank image to draw the contours on
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#Step6: drawing the contours on the blank image
#this function takes the blank image, contours, contour index and color as parameters
#contour index is -1 to draw all contours, color is a tuple of BGR
cv.drawContours(blank, contours, -1, (0,255,255), thickness=1)
cv.imshow('Contours on blank image', blank)

#Step7: drawing the contours on the original image
cv.drawContours(img, contours, -1, (0, 255, 255), tickness=1)
cv.imshow('Contours on Original Image', img)

cv.waitKey(0)


