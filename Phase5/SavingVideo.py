import cv2

# OPENNING THE CAMERA
camera = cv2.VideoCapture(0)


# GETTING THE HEIGHT AND WIDTH OF THE FRAME
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


# COMPRESSION FORMAT
codec = cv2.VideoWriter_fourcc(*'XVID')

# SAVING THE VIDEO
recorder = cv2.VideoWriter("my_vid.avi", codec, 20, (frame_width, frame_height))

while True:

    ret, frame = camera.read()

    if not ret:  

        print("Error")
        break

    recorder.write(frame)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):

        break

camera.release()
recorder.release()
cv2.destroyAllWindows()