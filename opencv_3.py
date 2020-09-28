import numpy as np
from cv2 import cv2

img = cv2.imread("images/image_2.jpg", cv2.IMREAD_COLOR)

# drawing a line
cv2.line(img, (100, 150), (150, 350), (255, 255, 255), 30)

# drawing a rectangle
cv2.rectangle(img, (500, 250), (1000, 500), (0, 155, 255), 15)

# drawing a circle
cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# drawing a polygon
pts = np.array([[100, 50], [200, 300], [700, 200], [500, 100]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

# writing some text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Hack", (10, 500), font, 2, (100, 155, 155), 3, cv2.LINE_AA)

# displaying the image
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()