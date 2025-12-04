import cv2

image = cv2.imread("C:\\Users\\abijit\\Desktop\\BgImage.jpg")

if image is not None:

    cv2.imwrite("Image.jpg", image)
    print("Image saved successfully !")
else:
    print("Error occurred !")