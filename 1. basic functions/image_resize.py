import imutils
import cv2

image = cv2.imread("images/venice.png")

# resize the image to 500x300px, ignoring aspect ratio
resized = cv2.resize(image, (500, 300))
cv2.imshow("Resized (ignored aspect ratio)", resized)
cv2.waitKey(0)

# fixed resizing with width=500px and the height based on the aspect ratio
(h, w, d) = image.shape
r = 500.0 / w
dim = (500, int(h*r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# using imutils library to resize the image (aspect ratio considered)
resized = imutils.resize(image, width=500)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)