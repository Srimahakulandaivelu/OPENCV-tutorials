import cv2 as cv

img = cv.imread('OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('cat', img)

# 1. converting the image to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. blurring the image to remove the noise present
#this function takes the image, kernel size and border type as parameters
#kernel size is the size of the filter used to blur the image, it should be odd
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. edge cascade: finding the edges in the image
#this function takes the image, threshold1 and threshold2 as parameters
#threshold1 is the lower threshold and threshold2 is the upper threshold
canny = cv.Canny(img, 100, 200)
cv.imshow('Canny Edges', canny)

#applying the canny edge detection on the blurred image
canny_blur = cv.Canny(blur, 100, 200)
cv.imshow('Canny Edges on Blurred Image', canny_blur)

# 4. dilating the image: increasing the thickness of the edges
#this function takes the image(edge detected), kernel and iterations as parameters
dilated = cv.dilate(canny_blur, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# 5. eroding the image: decreasing the thickness of the edges
#this function takes the image(dilated), kernel and iterations as parameters
eroded = cv.erode(dilated, (3,3), iterations=2)
cv.imshow('Eroded', eroded)

# 6. resizing the image
#this function takes the image and the new size as parameters
#the new size is a tuple of width and height
#the interpolation parameter is used to specify the method of resizing
# it can be cv.INTER_AREA, cv.INTER_LINEAR, cv.INTER_CUBIC, etc.
resized = cv.resize(img, (1500, 1500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)

# 7. cropping the image
#this is done by slicing the image array
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
