import cv2
import numpy as np

canvas = np.zeros((250,500,3), dtype="uint8");

# Rectangle
cv2.rectangle(canvas, (0,0), (300,150), (120,200,70), 3)

# Line
cv2.line(canvas, (310,160), (350,200), (255,0,0), 10)

# Circle
cv2.circle(canvas, (50,50), 30, (0,0,255), 1)

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, 'Hello Fraands!', (100,100), font, 1.25, (128,123,0), 2)

cv2.imshow('Drawing', canvas);
cv2.waitKey(0)
cv2.destroyAllWindows()