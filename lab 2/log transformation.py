import cv2
import numpy as np

img = cv2.imread('duck.jpg')
if img is None:
    raise FileNotFoundError("Could not load 'duck.jpg'")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

C = 20
log_img = C * np.log1p(gray_img.astype(np.float32))
log_img = cv2.normalize(log_img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

result = cv2.hconcat([gray_img, log_img])
cv2.imshow('Log transformation', result)
cv2.imwrite('output_image.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()