import cv2

ask = input("Can you please share the location of the image ? : ")

#load the image.
image = cv2.imread(ask)

while True:

    ask_again = input("Would you like to show the image or save the image ? (show/save/convert) : ").strip().lower()

    #showing the image
    if ask_again == "show":

        if image is not None:

            print("Image show successful")
            cv2.imshow("Image title !", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("error 1 occurred !")
    else:
        #saving the image.
        if ask_again == "save":

            if image is not None:   

                cv2.imwrite(image)
                print("Image saved successfully !")
            else:
                print("Error 2 occurred !")
        else:
            #convert the image.
            if ask_again == "convert":

                if image is not None:
                    
                    print("Image converted successfully !")
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Image title !", gray)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print("Error 4 occurred !")
            else:
                print("Check some default !")