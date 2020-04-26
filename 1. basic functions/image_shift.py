import cv2
import numpy as np

image = cv2.imread('images/image.jpg')
(height, width, dim) = image.shape

cv2.imshow("Original", image)
cv2.waitKey(0)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (width, height))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)