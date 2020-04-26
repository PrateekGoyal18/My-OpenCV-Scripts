import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# XVID is more preferable. MJPG results in high size video. X264 gives very small size video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.mp4',fourcc, 10.0, (640,480), isColor=True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()