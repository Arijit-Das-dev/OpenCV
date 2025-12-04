import cv2

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    cv2.putText(image, "Arijit Das", (300,300), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2 )
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")