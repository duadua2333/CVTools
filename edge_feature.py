# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import cv2
import numpy as np


def canny(img, save_src):
    """
    采用canny算子提取图像边缘特征
    :param img: 输入的图片
    :param save_src: 保存路径
    :return:
    """
    # 高斯模糊,降低噪声
    img = cv2.GaussianBlur(img, (3, 3), 0)
    # 灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 图像梯度
    xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
    ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)
    # 计算边缘
    # 50和150参数必须符合1：3或者1：2
    edge_output = cv2.Canny(xgrad, ygrad, 80, 240)
    cv2.imwrite(save_src, edge_output)


def sober(img, save_src):
    """
    采用sober算子提取图片边缘特征
    :param img: 输入的图片
    :param save_src: 保存路径
    :return:
    """
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)

    dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    cv2.imwrite(save_src, dst)


def laplacian(img, save_src):
    """
    采用拉普拉斯算子提取图片的边缘特征
    :param img: 输入的图片
    :param save_src: 保存路径
    :return:
    """
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将图像转化为灰度图像

    # 拉普拉斯边缘检测
    lap = cv2.Laplacian(image, cv2.CV_64F)  # 拉普拉斯边缘检测
    lap = np.uint8(np.absolute(lap))  # 对lap去绝对值
    cv2.imwrite(save_src, lap)


if __name__ == '__main__':
    src = "xxx"
    img_list = os.listdir(src)
    src2save = src + 'transformed/'
    for i in img_list:
        im = cv2.imread(src + i)
        canny(im, src2save)
        sober(im, src2save)
        laplacian(im, src2save)
