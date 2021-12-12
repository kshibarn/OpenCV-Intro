import cv2
import numpy as np

img = cv2.imread("E:/PyCharm Python/OpencvPython/Resources/Eternal.jpg")

width, height = 2100, 600
pts1 = np.float32([[781, 2359], [3053, 2399], [785, 2643], [3057, 2679]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)

cv2.waitKey(0)