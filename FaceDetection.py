import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'C:/Users/DELL/pythonvs/pixx/'
only = [b for b in listdir(data_path) if isfile(join(data_path, b))]
Training_data, labels = [], []

for i, files in enumerate(only):
    image_path = data_path + only[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_data.append(np.asarray(images, dtype=np.uint8))
    labels.append(i)
labels = np.asarray(labels, dtype=np.int32)
# print(type(labels))
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_data), np.asarray(labels))
print('Model Training done!')

face_classifier = cv2.CascadeClassifier(
    'C:/Users/DELL/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data'
    '/haarcascade_frontalface_default.xml')


def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img, []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))

    return img, roi


q = 0
e=0
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)
        confidence = int(100 * (1 - (result[1]) / 300))
        if result[1] < 500:

            # confidence=result[1] * 2.3
            # # print(result[1]*2)
            # # confidence = int(((result[1])/300))

            display_string = str(confidence) + '% Confidence it is the user'
            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)

        if confidence > 85:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)
            print(confidence)
            e=1
            q = q + 1

        else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)




    except:
        cv2.putText(image, "Face not found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass
    cv2.waitKey(1)
    if q == 5 and e==1:
            break

cap.release()
cv2.destroyAllWindows()
