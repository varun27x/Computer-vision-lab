import cv2
img = cv2.imread("duck.jpg")

cv2.putText(img, 'lab 1 ', (50, 200), cv2.FONT_HERSHEY_TRIPLEX,
            10, (0, 0, 0), 10, cv2.LINE_AA)

cv2.imshow('duck',img)
cv2.waitKey(0)
cv2.destroyAllWindows()