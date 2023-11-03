"""
    This script visualise the annotated data
        - only the specified ones

"""

import os
import matplotlib.pyplot as plt
import cv2
import numpy as np


def draw_annotation(image_name):
    image_path = os.path.join(os.path.dirname(os.getcwd()), "../data_set/image_dataset", image_name)
    annotation = image_name[:-4]
    annotation = annotation + ".txt"
    annotation_path = os.path.join(os.path.dirname(os.getcwd()), "src/labeled_dataset/obj_train_data/image_dataset", annotation)

    # coordinates for drawing
    x = list()
    y = list()

    # image shape
    image = cv2.imread(image_path)
    image_copy = image.copy()
    image_height = image.shape[0]
    image_width = image.shape[1]

    # box color
    color = [0, 0, 255]
    # get the annotation attributes
    with open(annotation_path) as fr:
        lines = fr.readlines()

    for line in lines:
        _, x, y, w, h = map(float, line.split(' '))
        x1 = int((x - w / 2) * image_width)
        x2 = int((x + w / 2) * image_width)
        y1 = int((y - h / 2) * image_height)
        y2 = int((y + h / 2) * image_height)

        if x1 < 0:
            x1 = 0
        if x2 > image_width - 1:
            x2 = image_width - 1
        if y1 < 0:
            y1 = 0
        if y2 > image_height - 1:
            y2 = image_height - 1

        # draw the rectangle into the image
        cv2.rectangle(image_copy, (x1, y1), (x2, y2), color, 2)

    plt.figure()
    plt.imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))


draw_annotation("35_1693139818.jpg")