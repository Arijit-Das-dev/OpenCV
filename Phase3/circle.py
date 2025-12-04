import cv2

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    center =(400, 400)
    radius = 50
    color = (0, 0, 255)
    thickness = 2

    cv2.circle(image, center, radius, color, thickness)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")
