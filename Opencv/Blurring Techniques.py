import  cv2 as cv

img = cv.imread('cat.jpg')
def rescaleFrame (frame,scale=0.20):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return  cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Orignal img', resized_img)

# Averaging
average = cv.blur(resized_img,(3,3))
cv.imshow('Average Blur', average)

#Gaussian blur
gauss = cv.GaussianBlur(resized_img,(3,3),0)
cv.imshow('Gaussian blur', gauss)

#Median Blur
median = cv.medianBlur(resized_img,3)
cv.imshow('Median BLur',median)

#Bilateral
bilateral = cv.bilateralFilter(resized_img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)