from matplotlib import pyplot as plt
import cv2

image = cv2.imread("images/beach.png")

# Grayscale Histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
hist = cv2.calcHist([gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Intensities")
plt.ylabel("No. of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

# Color Histogram
cv2.imshow("Original Image", image)
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Intensities")
plt.ylabel("No. of Pixels")
for (chan, color) in zip(chans, colors):
	hist = cv2.calcHist([chan], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)