import cv2
import numpy as np

image = cv2.imread("images/image.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

# --- rectangular mask ---
# cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)
# cv2.imshow("Mask", mask)
# cv2.waitKey(0)
# masked = cv2.bitwise_and(image, image, mask = mask)
# cv2.imshow("Mask Applied to Image", masked)
# cv2.waitKey(0)

# --- circular mask ---
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)