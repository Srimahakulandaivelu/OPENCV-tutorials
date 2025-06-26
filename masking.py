import cv2 as cv
import numpy as np

#masking is used to extract a region of interest from an image
#it is done by creating a mask of the region of interest and applying it to the image

img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('cat', img)

# Create a blank mask with the same dimensions as the image
blank = np.zeros(img.shape[:2], dtype='uint8')  
cv.imshow('Blank', blank)

# Create a circular mask
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) 
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 200, img.shape[0]//2 + 200), 255, -1)
cv.imshow('Rectangle Mask', rectangle)

# Combine the circle and rectangle masks
mask = cv.bitwise_or(circle, rectangle) 
cv.imshow('Combined Mask', mask)

# creating a masked image using the newly created mask
masked = cv.bitwise_and(img, img, mask= mask)
cv.imshow('Masked Image', masked)


cv.waitKey(0)
