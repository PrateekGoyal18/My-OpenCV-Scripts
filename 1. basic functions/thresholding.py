import cv2

# read the image
image = cv2.imread("images/coins.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", image)
cv2.waitKey(0)

# blurring the image to remove unwanted noise
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# threshold the image by setting all pixel values less than 155 to 255 (white; coins) 
# and all pixel values >= 155 to 255 (black; background)
(ret, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# applying the mask for coins detection
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=thresh))
cv2.waitKey(0)
cv2.destroyAllWindows()