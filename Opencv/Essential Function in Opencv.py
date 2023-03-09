import cv2 as cv

img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Image',resized_img)
# Converting to grayscale
gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#Blur the image
blur =cv.GaussianBlur(resized_img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#Edge Cascade
canny = cv.Canny(blur,125,175)
cv.imshow("Canny Edges",canny)

#Dilating the image

dilated = cv.dilate(canny,(3,3), iterations=1)
cv.imshow("Dilated img",dilated)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("eroded",eroded)

#Resize and crop
resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize",resize)

#croping
cropped = img[50:200 , 200:400]
cv.imshow("Crooped",cropped)


cv.waitKey(0)