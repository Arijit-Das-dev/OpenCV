import cv2

#load the image.
image = cv2.imread("C:\\Users\\abijit\\Desktop\\BgImage.jpg")

#you can crop the actual image or you can crop the resize image also.

if image is not None:

    resized = cv2.resize(image, (300, 300))
    cropped = resized[0:151, 0:151]

    cv2.imwrite("ResizeImage.jpg",resized)
    cv2.imshow("Resize image !",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("Cropped.jpg",cropped)
    cv2.imshow("Cropped !",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Some error occurred !")