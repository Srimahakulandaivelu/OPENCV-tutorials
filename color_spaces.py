import cv2 as cv
import matplotlib.pyplot as plt

#different libraries are used to display images in different color spaces
# OpenCV uses BGR color space by default, while matplotlib uses RGB color space

img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('Cat', img)

plt.imshow(img)  # Using matplotlib to display the image
plt.show()

# 1. converting the image to graysacle
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. converting the image to HSV (Hue, Saturation, Value) color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3. converting the image to LAB (Luminance, A, B) color space
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# 4. converting the image to RGB (Red, Green, Blue) color space
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Displaying the RGB image using matplotlib
plt.imshow(rgb)
plt.show()

# 5. converting the hsv image back to BGR color space
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

cv.waitKey(0)
