import cv2
import os


def text_reader():
    with open('C:\\Users\\19104\\内窥镜Paper\\OBRDataset\\video1_annot.txt', 'r') as f:
        rectangle_info = []
        rectangle_info_row = f.readlines()
        for i in range(len(rectangle_info_row)):
            column_list = rectangle_info_row[i].strip().split('\\n')
            temp = column_list[0].split()
            rectangle_info.append(temp)
        return rectangle_info


def img_marker(temp):
    path = 'video1'
    img_name_list = os.listdir(path)
    for i in range(len(img_name_list)):
        img_name = 'video1/' + img_name_list[i]
        img = cv2.imread(img_name)
        x = int(temp[i][0])
        y = int(temp[i][1])
        w = int(temp[i][2])
        h = int(temp[i][3])
        cv2.rectangle(img, (x, y), (w + w, y + h), (0, 255, 0,), 4)
        cv2.imwrite('video1_marked/' + img_name_list[i], img)


temp = text_reader()
img_marker(temp)
