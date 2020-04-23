import imutils
import cv2

image = cv2.imread("image.jpg")
(h, w, d) = image.shape

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2) # '//' to perform integer math (i.e., no floating point values).
M = cv2.getRotationMatrix2D(center, -45, 1) # '-' means clockwise
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)