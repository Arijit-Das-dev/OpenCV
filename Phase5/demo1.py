import cv2

# For openning the webcam
cap = cv2.VideoCapture(0)

'''
0 -> For internal device 
1 -> For external device 

'''
while True:

    ret, frame = cap.read() # if it returns true then it will open the webcam 

    if (not ret):

        print("Error")
        break

    cv2.imshow("Image", frame)

    if (cv2.waitKey(1)) & (0xFF) == ord('a'):

        print("Quitting")
        break

cap.release()
cv2.destroyAllWindows()