# coding: utf-8
# 导入相关库
import os
import cv2
import numpy as np
from json import dumps
# 要编码的图片文件

def image_json_t(c):
    i = 1
    while i !=c:
        IMAGE_NAME = 'image/Face_'+str(i)+'.jpg'

        if os.path.exists('image_json/opencv_temp_'+str(i)+'.json'):
          os.remove('image_json/opencv_temp_'+str(i)+'.json')
        # 保存为的json文件
        JSON_NAME = 'image_json/opencv_temp_'+str(i)+'.json'
        i += 1

        # 通过opencv读取图片
        img = cv2.imread(IMAGE_NAME)
        # numpy中ndarray文件转为list
        img_list = img.tolist()

        # 字典形式保存数组
        img_dict = {}
        img_dict['name'] = IMAGE_NAME
        img_dict['content'] = img_list

        # 保存为json格式
        json_data = dumps(img_dict, indent=2)
        # 将数据保存到文件
        with open(JSON_NAME, 'w') as json_file:
            json_file.write(json_data)
        print(i)
