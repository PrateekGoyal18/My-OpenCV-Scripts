import cv2

img_jpg = cv2.imread('image.jpg')
img_png = cv2.imwrite('image.png', img_jpg)
img_png = cv2.imread('image.png')
cv2.imshow('Image Show', img_png)
cv2.waitKey(0)
cv2.destroyAllWindows()