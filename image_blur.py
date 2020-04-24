import imutils
import cv2

image = cv2.imread("images/image.jpg")
(h, w, d) = image.shape

# Gaussian blur with a 9x9 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (9,9), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)