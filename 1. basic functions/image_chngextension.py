import cv2

img_jpg = cv2.imread('images/image.jpg')
img_png = cv2.imwrite('images/image.png', img_jpg)
img_png = cv2.imread('images/image.png')
cv2.imshow('Image Show', img_png)
cv2.waitKey(0)
cv2.destroyAllWindows()