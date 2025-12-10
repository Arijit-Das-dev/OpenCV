'''
Docstring for Phase6.Thresholding

Thresholding = convert pixel values into only black & white using a cutoff value. Useful for object segmentation.

what actually happens in Threshold ??

It converts pixels into B&W image based on their given range.

    ~ For each pixel value p:

    ~ If p > threshold → make it white (255)

    ~ Else → make it black (0)

'''

import cv2

image = cv2.imread("C:\\Users\\abijit\\Downloads\\FlowerImage.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresh_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

if image is None:

    print("error")

else:

    resized_actual_image = cv2.resize(image, (500, 500))
    resized_threshold_image = cv2.resize(thresh_image, (500, 500))

    cv2.imshow("actual image",resized_actual_image)
    cv2.imshow("threshold image", resized_threshold_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()