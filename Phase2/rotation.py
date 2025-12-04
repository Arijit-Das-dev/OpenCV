import cv2

image = cv2.imread("C:\\Users\\abijit\\Desktop\\BgImage.jpg")
if image is not None:
    
    (h, w) = image.shape[:2]
    
    center = (h//2, w//2)

    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (540, 960))
    
    cv2.imshow("Rotated_image", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error occurred !")