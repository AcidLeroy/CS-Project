from __future__ import print_function
import numpy as np
import pandas as pd
import cv2
import os


def create_ellipse_image(image, major_axis_radius, minor_axis_radius, angle, center_x, center_y,):
    new_image = np.zeros(image.shape, dtype=np.uint8)
    cv2.ellipse(new_image, (center_x,center_y), (major_axis_radius,minor_axis_radius), angle, 0, 360, 255, -1)
    return new_image

def create_rectangle_image(image, x, y, w, h):
    new_image = np.zeros(image.shape, dtype=np.uint8)
    cv2.rectangle(new_image, (x, y), (x + w, y + h), 255, -1)
    return new_image

def create_binary_image_from_rectangles(image, rectangles):
    new_image = np.zeros(image.shape())
    for (x, y, w, h) in rectangles:
        new_image = create_rectangle_image(new_image, x, y, w, h)
    return new_image

def create_binary_image_from_ellipses(image, ellipses):
     new_image = np.zeros(image.shape())
     for ellipse in ellipses:
         new_image = create_ellipse_image(new_image, ellipse[0], ellipse[1], ellipse[2], ellipse[3], ellipse[4])
     return new_image

def visit_all_images(path_to_hdf5):
    df = pd.read_hdf(path_to_hdf5, 'table')
    fddb_root = os.environ['FDDB_ROOT']  # Root directory of the FDDB dataset
    df = df.groupby('filename')
    for name, group in df:
        image_path = fddb_root +'/'+ name+'.jpg'
        #image = cv2.imread(name + '.jpg')
        print('File name is: ', image_path)
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

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
    visit_all_images(path_to_hdf5)

if __name__=='__main__':
    main()