from __future__ import print_function
import numpy as np
import pandas as pd
import cv2
import os
from FaceDetectHaar import FaceDetector
from sklearn.metrics import confusion_matrix


def create_ellipse_image(image, major_axis_radius, minor_axis_radius, angle, center_x, center_y,):
    #new_image = np.zeros(image.shape, dtype=np.uint8)

    major_axis_radius = int(round(float(major_axis_radius)))
    minor_axis_radius = int(round(float(minor_axis_radius)))
    angle = int(round(float(angle))) +90
    center_x = int(round(float(center_x)))
    center_y = int(round(float(center_y)))
    new_image = cv2.ellipse(image, (center_x, center_y), (major_axis_radius, minor_axis_radius), angle, 0, 360, 255, -1)
    return new_image

def create_rectangle_image(image, x, y, w, h):
    #new_image = np.zeros(image.shape, dtype=np.uint8)
    new_image = cv2.rectangle(image, (x, y), (x + w, y + h), 255, -1)
    return new_image

def create_binary_image_from_rectangles(image, rectangles):
    new_image = np.zeros(image.shape)
    for (x, y, w, h) in rectangles:
        new_image = create_rectangle_image(new_image, x, y, w, h)
    return new_image

def create_binary_image_from_ellipses(image, ellipses):
     new_image = np.zeros(image.shape)
     for ellipse in ellipses:
         new_image = create_ellipse_image(new_image, ellipse[0], ellipse[1], ellipse[2], ellipse[3], ellipse[4])
     return new_image

def get_ellipse_list(string_array):
    ellipses = []
    for entry in string_array:
        ellipses.append(entry.split())
    return ellipses

def get_ground_truth_image(grouped_dataframe, path_to_img, image):
     ellipses = grouped_dataframe.get_group(path_to_img)['ellipse'].tolist()
     ellipses = get_ellipse_list(ellipses)
     ground_truth_image = create_binary_image_from_ellipses(image, ellipses)
     return ground_truth_image


def compare_to_truth(path_to_hdf5):
    df = pd.read_hdf(path_to_hdf5, 'table')
    fddb_root = os.environ['FDDB_ROOT']  # Root directory of the FDDB dataset
    df = df.groupby('filename')
    metric = np.zeros((2,2))
    for name, group in df:
        image_path = fddb_root +'/'+ name+'.jpg'
        print('File name is: ', image_path)
        fd = FaceDetector()
        image = fd.retrieve_image(image_path)
        ground_truth = get_ground_truth_image(df, name, image)

        rectangles = fd.apply_all_cascades(image)
        predicted_faces = create_binary_image_from_rectangles(image, rectangles)

        single_metric = confusion_matrix(ground_truth.ravel(), predicted_faces.ravel())
        metric = metric + single_metric
        # print(metric)
        #
        #
        # cv2.imshow('ground_truth', ground_truth)
        # cv2.imshow('predicted_faces', predicted_faces)
        # cv2.imshow('original_image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    return metric

def main():
    # img = np.zeros((512,512), np.uint8)
    # #cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
    # new_image = create_ellipse_image(img, 100, 50, 0, 256, 256)
    # cv2.imshow('ellipse', new_image)
    #
    # rect_image = create_rectangle_image(img, 256, 256, 100, 100)
    # cv2.imshow('rectangle', rect_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    path_to_hdf5 = '/Users/cody/face_data_png/FDDB-folds/fddb_ellipse.h5'
    confusion_mat = compare_to_truth(path_to_hdf5)
    print(confusion_mat)


if __name__=='__main__':
    main()