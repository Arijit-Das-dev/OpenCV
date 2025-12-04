import cv2

image = cv2.imread("C:\\Users\\abijit\\OneDrive\\Desktop\\BgImage.jpg")

if image is not None:

    try :

        cv2.imshow("Your iamge !", image) #show the image.
        cv2.waitKey(0) #holds the image.
        cv2.destroyAllWindows() #close the image after any operation by user.
        print("Image loaded successfully !")
    
    except Exception as e:

        print(f"{e}")

else:
    print("Error occurred !")