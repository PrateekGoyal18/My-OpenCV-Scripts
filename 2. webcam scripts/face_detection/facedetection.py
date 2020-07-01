import cv2
import imutils

class FaceDetector:
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        
    def detect(self, image, scaleFactor, minNeighbors, minSize):
        rects = self.faceCascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize, flags=cv2.CASCADE_SCALE_IMAGE)
        return rects

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise IOError("Cannot open webcam")
fd = FaceDetector("haarcascade_frontalface_default.xml")

while(True):
    (ret, frame) = camera.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faceRects = fd.detect(gray, scaleFactor=1.2, minNeighbors=3, minSize=(20, 20))
    frameClone = frame.copy()
    for (fX, fY, fW, fH) in faceRects:
        cv2.putText(frameClone, str(len(faceRects))+" persons found!", (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0 , 255), 2)
        cv2.rectangle(frameClone, (fX, fY), (fX+fW, fY+fH), (0, 255, 0), 2)
    cv2.imshow("Face", frameClone)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()