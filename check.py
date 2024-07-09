import cv2

cap = cv2.VideoCapture(0)  # Ensure you are using the correct camera index

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 27:  # Press Esc to exit
        break

cap.release()
cv2.destroyAllWindows()

