import cv2

img = cv2.imread('duck.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

neg = cv2.bitwise_not(gray)

cv2.imshow('Input Image', img)
cv2.imshow('Negative Image', neg)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('negative_image.jpg', neg)

cv2.destroyAllWindows()
