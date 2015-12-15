import cv2
import os
import numpy as np

class FaceDetector(object):
    def __init__(self):
        cv_root = os.environ['OPENCV_ROOT']
        self.cascades = {'frontal': cv2.CascadeClassifier(
                            cv_root + '/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml'),
                        'profile': cv2.CascadeClassifier(
                            cv_root + '/usr/local/share/OpenCV/haarcascades/haarcascade_profileface.xml')}

    def retrieve_image(self, path_to_image):
        image = cv2.imread(path_to_image, 0)
        return image

    def detect_faces(self, image, cascade_type):
        faces = cascade_type.detectMultiScale(image, 1.3, 5)
        return faces

    def draw_rectangles(self, image, rectangles, color=(255, 255, 255)):
        for (x, y, w, h) in rectangles:
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        return image

    def apply_all_cascades(self, image):
        rectangles = np.array([])
        for cascade in self.cascades:
            rects = self.detect_faces(image, self.cascades[cascade])
            if type(rects) is np.ndarray:
                rectangles = np.vstack([rectangles, rects]) if rectangles.size else rects
        return rectangles


    def apply_gaussian_blur(self, image, rectangles):
        for (x, y, w, h) in rectangles:
            image[y:y + h, x:x + w] = cv2.GaussianBlur(image[y:y + h, x:x + w], (25, 25), 10)
        return image


def main():
    face = FaceDetector()
    fddb_root = os.environ['FDDB_ROOT']  # Root directory of the FDDB dataset
    path_to_image = fddb_root + '/2002/08/07/big/img_1209.jpg'
    print(path_to_image)
    image = face.retrieve_image(path_to_image)
    rectangles = face.apply_all_cascades(image)

    new_image = face.apply_gaussian_blur(image, rectangles)
    cv2.imshow('new_image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
