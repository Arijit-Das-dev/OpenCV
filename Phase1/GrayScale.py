import cv2

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image title !",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error occurred !")