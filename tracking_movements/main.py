import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# Read first frame
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # Find difference between two frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate to fill gaps
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find moving object contours
    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw rectangle around movement
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Movement Detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show output
    cv2.imshow("Movement Tracking", frame1)

    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    # Press q to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()