import cv2
image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    h, w, c = image.shape
    print(f"Height : {h}\nWidth : {w}\nColor channels : {c}")
    
else:
    print("Error occurred !")