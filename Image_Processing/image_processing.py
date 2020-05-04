import cv2

img = cv2.imread(r"Image_Processing\image.jpg", 0)
resized_image = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/4)))
cv2.imshow("Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()