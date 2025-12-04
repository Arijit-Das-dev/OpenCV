import cv2

image = cv2.imread("C:\\Users\\abijit\\Desktop\\BgImage.jpg")

if image is not None:


    resize = cv2.resize(image, (300, 300))
    flip_horizentally = cv2.flip(resize, 1) 
    flip_vertically = cv2.flip(resize, 0)
    flip_both = cv2.flip(resize, -1)

    cv2.imshow("Horizontally",flip_horizentally)
    cv2.imshow("Vertically",flip_vertically)
    cv2.imshow("Flip both",flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error occurred !")