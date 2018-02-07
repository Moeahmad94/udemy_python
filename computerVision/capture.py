import cv2, time

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    cv2.waitKey(16)

    if key==ord('q')
        break

video.release()
cv2.destroyAllWindows()
