import cv2

#load the image.
image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    print("Image loaded successfully !")
else:
    print("Error occurred !")