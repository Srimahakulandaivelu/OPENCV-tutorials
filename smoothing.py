import cv2 as cv

img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('Cat', img)

# 1. average blurring: averaging the pixel values in a neighborhood
average_blur = cv.blur(img, (3,3))
cv.imshow('Average Blur', average_blur)

# 2. gaussian blurring: averaging the pixel values in a neighborhood with a Gaussian kernel
#this function takes the image, kernel size and sigma value as parameters
# kernel size must be odd and positive, sigma value is the standard deviation of the Gaussian distribution
gaussian_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian_blur)

# 3. median blurring: replacing each pixel value with the median value in a neighborhood and is useful for removing salt and pepper noise
median_blur = cv.medianBlur(img, 3)
cv.imshow('Median blur', median_blur)

# 4. bilateral blurring: averaging the pixel values in a neighborhood while preserving edges
# this function takes the image, diameter of the pixel neighborhood, sigma color and sigma space as parameters
bilateral_blur = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Blur', bilateral_blur)


cv.waitKey(0)
