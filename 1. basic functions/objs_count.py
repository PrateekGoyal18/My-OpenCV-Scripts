import cv2

# read the image
image = cv2.imread("images/coins.png")
cv2.imshow("Image", image)
cv2.waitKey(0)

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# applying edge detection we can find the outlines of objects in image
edged = cv2.Canny(gray, 50, 100)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
ret, thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)


# For better accuracy, use binary images. 
# So before finding contours, apply threshold or canny edge detection.

# findContours function modifies the source image. 
# So if you want source image even after finding contours, already store it to some other variables.

# In OpenCV, finding contours is like finding white object from black background. 
# So remember, object to be found should be white and background should be black.
cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = image.copy()
# loop over the contours
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], 0, (240, 0, 159), 3)
	cv2.imshow("Contours", output)
	cv2.waitKey(0)

# draw the total number of contours found in purple
text = "Found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)