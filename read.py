import cv2 as cv

# code to read an image and display it
img = cv.imread('OPENCV TUTORIALS\\photos\\cat1.jpeg')

if img is None:
    print("Error: No image found")
else:
    cv.imshow('cat', img)
    cv.waitKey(0)


# code to read a video file and display it frame by frame
capture = cv.VideoCapture('OPENCV TUTORIALS\\videos\\1182756-hd_1920_1080_25fps.mp4')

while True:
    isTrue, frame= capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('g'):
        break

capture.realease()
cv.destroyAllWindows()
