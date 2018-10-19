import os

import cv2 as cv


def edge(img, i):
    # 高斯模糊,降低噪声
    img = cv.GaussianBlur(img, (3, 3), 0)
    # 灰度图像
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    # 图像梯度
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # 计算边缘
    # 50和150参数必须符合1：3或者1：2
    edge_output = cv.Canny(xgrad, ygrad, 80, 240)
    cv.imwrite('temp/'+i, edge_output)


en_list = os.listdir("C:/Users/duadua/PycharmProjects/Endoscope/video1/")
for i in en_list:
    im = cv.imread("C:/Users/duadua/PycharmProjects/Endoscope/video1/" + i)
    edge(im, i)
