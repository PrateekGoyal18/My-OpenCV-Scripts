import cv2

img_png = cv2.imread('images/venice.png')
img_jpg = cv2.imwrite('images/venice.jpg', img_png)
img_jpg = cv2.imread('images/venice.jpg')

cv2.imshow('Image .png format (Original)', img_png)
cv2.imshow('Image .jpg format (Converted)', img_png)
cv2.waitKey(0)
cv2.destroyAllWindows()