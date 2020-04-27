import cv2
import numpy as np

image = cv2.imread("images/beach.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

(cX, cY) = (image.shape[1]//2, image.shape[0]//2)

# --- rectangular mask ---
mask_rect = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask_rect, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
cv2.imshow("Rectangular Mask", mask_rect)
cv2.waitKey(0)
masked = cv2.bitwise_and(image, image, mask=mask_rect)
cv2.imshow("Rectangular Mask Applied to Image", masked)
cv2.waitKey(0)

# --- circular mask ---
mask_cir = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask_cir, (cX, cY), 100, 255, -1)
cv2.imshow("Circular Mask", mask_cir)
cv2.waitKey(0)
masked = cv2.bitwise_and(image, image, mask=mask_cir)
cv2.imshow("Circular Mask Applied to Image", masked)
cv2.waitKey(0)