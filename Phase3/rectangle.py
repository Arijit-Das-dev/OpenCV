import cv2

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    resized = cv2.resize(image, (400, 400))

    pt1 = (100, 200)
    pt2 = (300, 210)
    color = (0, 0, 255)
    thickness = 2
    
    cv2.rectangle(resized, pt1, pt2, color, thickness)
    cv2.imshow("image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
else:
    print("Error")