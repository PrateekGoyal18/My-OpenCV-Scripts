import cv2
import numpy as np

image = cv2.imread("images/wave.png")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# splitting
(B, G, R) = cv2.split(image)
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", R)
cv2.imshow("Red (Actual Color)", cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.imshow("Green (Actual Color)", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.imshow("Blue", B)
cv2.imshow("Blue (Actual Color)", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

# merging
merged = cv2.merge([B, G, R])
cv2.imshow("Original Image (Merged after split)", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()