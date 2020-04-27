import imutils
import cv2

image = cv2.imread("images/venice_small.png")
(h, w, d) = image.shape

# Gaussian blur with a 9x9 kernel to the image to smooth it, useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (9,9), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# looping in blurring
for i in range(1,20,2):
	blurred = cv2.GaussianBlur(image, (i,i), 0)
	image_name = "Blurring with kernel size (" + str(i) + "," + str(i) + ")"
	cv2.imshow(image_name, blurred)
	cv2.waitKey(0)
	cv2.destroyAllWindows()