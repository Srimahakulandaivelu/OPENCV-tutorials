import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('cat', img)

# finding the histogram of grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Create a blank mask with the same dimensions as the image
blank = np.zeros(img.shape[:2], dtype='uint8')  
cv.imshow('Blank', blank)

# Create a circular mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 250, 255, -1) 
cv.imshow('Mask', mask)

# creating a masked image using the newly created mask
masked = cv.bitwise_and(gray, gray, mask= mask)

gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# finding the histogram of colored image
colors = ('b', 'g', 'r')

plt.figure()

for i,colors in enumerate(colors):
    hist = cv.calcHist([img], [i], masked, [256], [0,256])
    plt.plot(hist, color=colors)
    plt.xlim([0, 256])

plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')   
plt.show()


cv.waitKey(0)
