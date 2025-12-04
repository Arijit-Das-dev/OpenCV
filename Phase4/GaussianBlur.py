import cv2

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    blurrImage = cv2.GaussianBlur(image, (7, 7), 0)

    cv2.imshow("image",blurrImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:

    print("Error")