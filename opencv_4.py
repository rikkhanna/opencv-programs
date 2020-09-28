from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/image_3.jpg", cv2.IMREAD_COLOR)

px = img[55, 55]  # referencing specific pixels

img[55, 55] = [255, 255, 255]  # change a pixel with white color

px = img[55, 55]  # re-referrencing
print(px)

px = img[100:150, 100:150]  # referencing ROI - Region of image
print(px)

img[100:150, 100:150] = [255, 255, 255]  # modifying the ROI

# reference certain characteristics of our image:
print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[100:600, 500:1000]
img[0:500, 0:500] = watch_face

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.show()

# cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()