import cv2
import numpy as np

def cartoon_rendering(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (500, 500))
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.medianBlur(gray, 5)
    
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)
    
    color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)
    
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

image_path = "image.jpg"

output_image = cartoon_rendering(image_path)

cv2.imshow("Cartoon Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
