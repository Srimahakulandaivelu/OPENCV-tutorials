import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('Cat', img)

# Step 1: Splitting the image into its color channels
b, g, r = cv.split(img)

cv.imshow('Blue Channel', b)
cv.imshow('Green Channel', g)
cv.imshow('Red channel', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Step 2: Merging the color channels back into a single image
merged = cv.merge([b, g, r])
cv.imshow('Merged image', merged)

# Step 3: Creating a blank image with the same dimensions as the original image to visualize each channel
blank = np.zeros(img.shape[:2], dtype = 'uint8')

blue = cv.merge([b, blank, blank])
cv.imshow('Blue Channel Image', blue)

green = cv.merge([blank, g, blank])
cv.imshow('Green Channel Image', green)

red = cv.merge([blank, blank, r])
cv.imshow('Red Channel Image', red)


cv.waitKey(0)
