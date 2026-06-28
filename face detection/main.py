import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# Read image
#img = cv2.imread("single_face.jpeg")
img = cv2.imread("group_face.jpeg")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show grayscale image
cv2.imshow("Grayscale Image", gray)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Show final image
cv2.imshow("Detected Faces", img)

# Save output
cv2.imwrite("detected_face.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()