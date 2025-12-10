'''
Docstring for Phase6.CannyEdgeDetection

"CANNY EDGE DETECTION"

That function used for detecting all the edges of any image.

Usage :

1> Edge detection
2> Seperate objects in a image
3> Feature Extraction

'''


import cv2

image = cv2.imread("C:\\Users\\abijit\\Downloads\\FlowerImage.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:

    resized_image = cv2.resize(image, (600, 600))

    cv2.imshow("Image", resized_image)
    edge = cv2.Canny(resized_image, 50, 150)
    cv2.imshow("Image 2", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:

    print("Error")