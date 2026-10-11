import cv2
image1=cv2.imread("Special Effects/ironman.jpg")
cv2.imshow("ironman",image1)
cv2.waitKey(0)
gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)#converting into grey scale
blur=cv2.medianBlur(gray,5)#converting it to blue
edges=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)#according to the average paremeters of the immage we are defining the range of getting the images blurred
color=cv2.bilateralFilter(image1,9,250,250)#converting back into the color format
cartoon=cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("cartoon image",cartoon)
cv2.waitKey()
cv2.destroyAllWindows()