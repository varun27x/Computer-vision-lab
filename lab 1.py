import cv2
img = cv2.imread("duck.jpg")
cv2.imshow('duck',img)
cv2.waitKey(0)
cv2.destroyAllWindows()