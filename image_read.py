import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("image.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

# access the RGB pixel located at x=200, y=400
# keep in mind that the height is the number of rows and the width is the number of columns
(B, G, R) = image[400, 200]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=450,y=350 at ending at x=650,y=475
roi = image[350:500, 450:650]
cv2.imshow("ROI", roi)
cv2.waitKey(0)