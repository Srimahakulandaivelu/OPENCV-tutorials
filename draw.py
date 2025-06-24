import cv2 as cv
import numpy as np

#creating a blank image to draw shapes upon
blank = np.zeros((500, 500, 3), dtype = 'uint8') #this dtype is used to create a blank image of 500x500 pixels
cv.imshow('Blank', blank)

#1. painting the image with a colour
blank[:] = 0,0,255
cv.imshow('Red', blank)

#2. drawing a rectangle
#this rectangle function takes the image, starting point, ending point, colour and thickness as parameters
cv.rectangle(blank, (50,50), (250,250), (0,0,0), thickness = cv.FILLED) #cv.FILLED is used to fill the rectangle with colour
cv.imshow('Rectangle', blank)

#3.drawing a circle
#this circle function takes the image, center point, radius, colour and thickness as parameters
#thickness = 2 means the circle will be drawn with a thickness of 2 pixels
cv.circle(blank, (251,251), 50, (255,0,0), thickness = cv.FILLED)
cv.imshow('Circle', blank)

#4. drawing a line
#this line function takes the image, starting point, ending point, colour and thickness as parameters
cv.line(blank, (280,280), (499,499), (0,255,0), thickness = 3) 
cv.imshow('Line', blank)

#write text on a image
#this function takes image, text, point, fontFace, fontScale, colour and thickness as parameters
cv.putText(blank, 'Hello, gurlss!!', (100, 300),fontFace=cv.FONT_ITALIC, fontScale=2, color=(255,255,255),thickness=5)
cv.imshow('Text', blank)

cv.waitKey(0)
