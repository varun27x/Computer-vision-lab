import cv2
import numpy as np
img = cv2.imread('duck.jpg')
cv2.circle(img, center=(100, 100), radius=50, color=(0, 255, 0), thickness=2)
cv2.rectangle(img, (50, 50), (300, 200), (255, 0, 0), 3)
cv2.imshow('duck',img)
cv2.waitKey(0)
cv2.destroyAllWindows()