def picture(imagePath):
    import cv2

    img = cv2.imread(imagePath)

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=7, minSize=(40, 40)
    )

    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
