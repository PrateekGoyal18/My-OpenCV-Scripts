import imutils
import cv2

image = cv2.imread("images/venice_small.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# 1 indicates that we are going to flip the image horizontally, around the y-axis
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

# 0 indicates that we want to flip the image vertically, around the x-axis
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

# using a negative flip code (Line 18) flips the image around both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)