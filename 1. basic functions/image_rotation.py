import imutils
import cv2

image = cv2.imread("images/image.jpg")
(h, w) = image.shape[:2]

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2) # '//' to perform integer math (i.e., no floating point values).
M = cv2.getRotationMatrix2D(center, -45, 1.0) # '-' means clockwise and the last parameter is image scale
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# # rotation can also be easily accomplished via imutils with less code
# rotated = imutils.rotate(image, -45)
# cv2.imshow("Imutils Rotation", rotated)
# cv2.waitKey(0)

# # OpenCV doesn't "care" if our rotated image is clipped after rotation
# # so we can instead use another imutils convenience function to help us out
# rotated = imutils.rotate_bound(image, -45)
# cv2.imshow("Imutils Bound Rotation", rotated)
# cv2.waitKey(0)