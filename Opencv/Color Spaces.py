import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)

#BGR ro RGB
plt.imshow(resized_img)
plt.show()


#BGR to Grayscale

gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

#BGR to HSV

hsv = cv.cvtColor(resized_img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to LAB

lab = cv.cvtColor(resized_img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR to RGB

rgb = cv.cvtColor(resized_img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#HSV or LAB or RGB or GRAYSCALE to BGR

hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV2BGR',hsv_bgr)



cv.waitKey(0)