import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from image_json import image_json_t
import os
from json import dumps
from sys import argv
from base64 import b64encode

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(
        "C:/Windows/Fonts/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)
#
# def face_detect(img):
#     #fourcc = cv.VideoWriter_fourcc(*'XVID')  # 保存视频的编码
#     #out = cv.VideoWriter('output.mp4', fourcc, 19.0, (640, 480))
#     gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     face_detecter = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
#     face = face_detecter.detectMultiScale(gray,1.1,2)
#     for x,y,w,h in face:
#
#         cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#         cv.rectangle(img, (x, y), (x + 60, y - 30), (0, 0, 0), 2)
#         img =cv2ImgAddText(img, "脸", x + 25, y - 25)
#
#         cv.putText(img, "face", (x+5,y-5), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 1)
#     # out.write(img)
#
#
#     cv.imshow("a",img)
#     return img

# def JSON_img(img):
#    IMAGE_NAME = img
#    JSON_NAME = 'opencv_temp.json'
#    img_1 = cv.imread(img)
#    img_list = img_1.tolist()
#    img_dist = {}
#    img_dist['content']=img_list_

cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')  # 保存视频的编码
out = cv.VideoWriter('output.mp4', fourcc, 19.0, (640, 480))
c=1
a=True
while (cap.isOpened()):
    ret, img = cap.read()
    if os.path.exists('image/Face_'+str(c)+'.jpg'):
        os.remove('image/Face_'+str(c)+'.jpg')

    cv.imwrite('image/Face_' + str(c) + '.jpg', img)

    c = c + 1
    cv.waitKey(1)
    if True:
        # face_detect(frame)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_detecter = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        face = face_detecter.detectMultiScale(gray, 1.1, 2)
        for x, y, w, h in face:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv.rectangle(img, (x, y), (x + 60, y - 30), (255, 0, 255), 2)
            img = cv2ImgAddText(img, "脸", x + 25, y - 25)
            # cv.putText(img, "face", (x + 5, y - 5), cv.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 1)
        # frame = cv.flip(frame,1)
        # write the flipped frame
        out.write(img)
        cv.imshow('frame', img)
        #JSON_img(img)


        if cv.waitKey(10) == 27:
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
print(c)
image_json_t(c)