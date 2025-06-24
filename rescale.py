import cv2 as cv

# this function takes the frames of images and videos to resize them to the scale specified
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) # shape[1] is the width of the frame 
    height = int(frame.shape[0] * scale) # shape[0] is the height of the frame

    dimensions = (width, height) # dimensions is a tuple of width and height

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) #interpolation is used to rescale the frame

capture = cv.VideoCapture('OPENCV TUTORIALS\\videos\\dog.mp4.mp4')

while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame, 0.5)

    cv.imshow("video", frame)
    cv.imshow("Resized video", resized_frame)

    if cv.waitKey(20) & 0xFF == ord('g'):
        break

capture.realease()
cv.destroyAllWindows()

