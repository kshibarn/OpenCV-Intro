import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
img[:] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 4)
cv2.rectangle(img, (0, 0), (300, 450), (0, 255, 0), 1)
cv2.circle(img, (500, 100), 10, (255, 200, 0), 4)
cv2.putText(img, "Open-CV", (200, 75), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 4)

cv2.imshow("Image", img)

cv2.waitKey(0)