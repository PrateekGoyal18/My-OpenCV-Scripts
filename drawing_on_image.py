import cv2

image = cv2.imread("images/image.jpg")
output = image.copy()

cv2.line(output, (165, 542), (775, 542), (0, 0, 255), 5)
cv2.rectangle(output, (475, 375), (620, 490), (0, 0, 255), 3)
cv2.circle(output, (785, 480), 20, (255, 0, 0), 2)
cv2.circle(output, (140, 390), 20, (255, 0, 0), 2)
cv2.putText(output, "OpenCV + Venice :)", (100, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)

cv2.imshow('drawing', output)
cv2.waitKey(0)