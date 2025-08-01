
import cv2
# open the video file
cap = cv2.VideoCapture('random_video.mp4')
# loop through frames in the video
while cap.isOpened():

    ret, frame = cap.read()
    # check if the frame was successfully read
    if ret:

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else:
            break
# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
