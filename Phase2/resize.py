import cv2

image = cv2.imread("C:\\Users\\abijit\\Desktop\\BgImage.jpg")

if image is not None:

    resized = cv2.resize(image, (300, 300))
    cv2.imshow("Actual Image ", image)
    cv2.imwrite("Image2.jpg",resized)
    cv2.imshow("Resized image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Some errors occurred !")