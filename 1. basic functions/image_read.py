import cv2

# load the input image and show its dimensions
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
# width*height = cols*rows = x*y and in opencv it's always the other way round while writing code
image = cv2.imread("images/venice.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# display the image to our screen and press a key on the keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

# access the RGB pixel located at x=200, y=400
# keep in mind that the height is the number of rows and the width is the number of columns
(B, G, R) = image[400, 200]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=450,y=350 at ending at x=650,y=500
roi = image[350:500, 450:650]
cv2.imshow("ROI", roi)
cv2.waitKey(0)