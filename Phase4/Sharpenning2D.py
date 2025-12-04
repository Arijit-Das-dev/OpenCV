import cv2 
import numpy as np

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

sharp = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])

if image is not None:

    sharpened = cv2.filter2D(image, -1, sharp)
    cv2.imshow("image",sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    
    print("Error...")