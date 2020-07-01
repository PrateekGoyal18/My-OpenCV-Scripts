import cv2
import numpy as np

image = cv2.imread("images/beach.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

M = np.ones(image.shape, dtype="uint8")*100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

M = np.ones(image.shape, dtype="uint8")*50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)