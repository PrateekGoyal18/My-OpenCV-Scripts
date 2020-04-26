import cv2

# Define a camera object
cap = cv2.VideoCapture(0)

# Check if camera is opened or not
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while(True):
    # Start reading the frames
    ret, frame = cap.read()
    
    # Get the frames properties
    width = cap.get(3)
    height = cap.get(4)
    fps = cap.get(5)
    print("width={}, height={}, fps={}".format(width, height, fps))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()