import cv2 

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:

        print("Error")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):

        print("quitting")
        break

cap.release()
cv2.destroyAllWindows()