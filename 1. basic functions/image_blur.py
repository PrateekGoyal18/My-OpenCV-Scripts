import imutils
import cv2

image = cv2.imread("images/venice_small.png")

# --------- Average Blur ---------
# blur with a 9x9 kernel
blurred = cv2.blur(image, (9,9))
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# looping in blurring
for i in range(1,20,2):
	blurred = cv2.blur(image, (i,i), 0)
	image_name = "Average Blurring with kernel size (" + str(i) + "," + str(i) + ")"
	cv2.imshow(image_name, blurred)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# --------- Gaussian Blur ---------
# blur with a 9x9 kernel
blurred = cv2.GaussianBlur(image, (9,9), 0)
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# looping in blurring
for i in range(1,20,2):
	blurred = cv2.GaussianBlur(image, (i,i), 0)
	image_name = "Gaussian Blurring with kernel size (" + str(i) + "," + str(i) + ")"
	cv2.imshow(image_name, blurred)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# --------- Median Blur ---------
# blur with a 9x9 kernel
blurred = cv2.medianBlur(image, 9)
cv2.imshow("Median", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# looping in blurring
for i in range(1,20,2):
	blurred = cv2.medianBlur(image, i)
	image_name = "Median Blurring with kernel size " + str(i)
	cv2.imshow(image_name, blurred)
	cv2.waitKey(0)
	cv2.destroyAllWindows()