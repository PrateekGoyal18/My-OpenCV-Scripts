import cv2
import imutils

class EyeTracker:
	def __init__(self, faceCascadePath, eyeCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
		self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

	def track(self, image):
		faceRects = self.faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
		rects = []

		for (fX, fY, fW, fH) in faceRects:
			faceROI = image[fY:fY+fH, fX:fX+fW]
			rects.append((fX, fY, fX+fW, fY+fH))
			eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor=1.1, minNeighbors=10,minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
			for (eX, eY, eW, eH) in eyeRects:
				rects.append((fX+eX, fY+eY, fX+eX+eW, fY+eY+eH))
		return rects

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise IOError("Cannot open webcam")
et = EyeTracker("haarcascade_frontalface_default.xml", "haarcascade_eye.xml")

while True:
	(grabbed, frame) = camera.read()
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = et.track(gray)
	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
	cv2.imshow("Tracking", frame)
	
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()