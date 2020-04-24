import imutils
import cv2

image = cv2.imread("images/image.jpg")

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# # fixed resizing and distort aspect ratio so let's resize the width
# # to be 500px but compute the new height based on the aspect ratio
# (h, w, d) = image.shape
# r = 500.0 / w
# dim = (500, int(h*r))
# resized = cv2.resize(image, dim)
# cv2.imshow("Aspect Ratio Resize", resized)
# cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=500)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)