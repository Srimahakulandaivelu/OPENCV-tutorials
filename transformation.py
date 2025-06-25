import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\Srimaha K\\OneDrive\\Documents\\Desktop\\OPENCV TUTORIALS\\photos\\cat2.jpg')
cv.imshow('cat', img)

#1. translation: moving the image in x and y direction
# this function takes the image, x and y translation values as parameters
# x is the translation in the horizontal direction and y is the translation in the vertical direction

#-x = left shift
#-y = up shift
#x = right shift
#y = down shift

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) # to find the translation matrix, we use np.float32 to convert the matrix to float type
    dimensions = (img.shape[1], img.shape[0])
    
    translated = cv.warpAffine(img, transMat, dimensions)
    return translated

translated_img = translate(img, 100, 200)
cv.imshow('Translated', translated_img)

# 2.rotation: rotating the image around the center
# this function takes the image, angle of rotation and center of rotation as parameters
def rotate(img, angle, rotpoint = None):
    (height, width) = (img.shape[0], img.shape[1])

    if rotpoint is None:  #if no rotation point is specified, use the center of the image
        rotpoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0) # to find the rotation matrix
    dimensions = (width, height)

    rotated = cv.warpAffine(img, rotMat, dimensions)  # to rotate the image
    return rotated

rotated_img = rotate(img, 45)
cv.imshow('Rotated', rotated_img)

# 3. flipping: flipping the image horizontally or vertically
# this function takes the image and flip code as parameters
flip = cv.flip(img, -1)  # 0 for vertical flip, 1 for horizontal flip, -1 for both
cv.imshow('Flipped', flip)

# 4. resizing: resizing the image to a new size
# this function takes the image and the new size as parameters  
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)  # new size is a tuple of width and height
cv.imshow('Resized', resized)

# 5. cropping: cropping the image to a specific region
# this is done by slicing the image array
cropped = img[50:250, 250:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
