import cv2

#haaroascade 불러오기 - 얼굴과 눈을 찾기 위해 미리 학습된 샘플 데이터
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#이미지 불러오기
img = cv2.imread('image2.jpg')

#이미지 전처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
imgNum = 0
for (x,y,w,h) in faces:
    #얼굴만 자르기
    cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]

    #자른 이미지 저장
    cv2.imwrite("face" + str(imgNum) + ".png", cropped)
    new_img = cv2.imread("face" + str(imgNum) + ".png")
    imgNum += 1

# 결과 출력
cv2.imshow('Image view', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()