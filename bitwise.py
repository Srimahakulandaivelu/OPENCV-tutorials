import cv2 as cv
import numpy as np

# creating two images like rectangle and circle to apply bitwise operations
blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# 1. Bitwise AND operation : this operation returns the intersection of two images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# 2. Bitwise OR operation : this operation returns the union of two images
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# 3. Bitwise XOR operation : this operation returns the pixels that are in either of the images but not in both
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# 4. Bitwise NOT operation : this operation inverts the pixels of the image
bitwise_not_rectangle = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT Rectangle', bitwise_not_rectangle)   

bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT Circle', bitwise_not_circle)

cv.waitKey(0)
