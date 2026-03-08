import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Microscope Camera Feed", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("captured_image.jpg", frame)
        print("Image Saved")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()