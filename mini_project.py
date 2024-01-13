import cv2
image = cv2.imread("Dog.jpg")
height = image.shape[0]
width = image.shape[1]
h = int(height*0.5)
w = int(width*0.5)
Resized_image = cv2.resize(image,(h,w), interpolation=cv2.INTER_AREA)
cv2.imshow("Dog", Resized_image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(Resized_image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)