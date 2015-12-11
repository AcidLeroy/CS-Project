import numpy as np
import cv2

def create_ellipse_image(image, major_axis_radius, minor_axis_radius, angle, center_x, center_y,):
    new_image = np.zeros(image.shape, dtype=np.uint8)
    cv2.ellipse(new_image, (center_x,center_y), (major_axis_radius,minor_axis_radius), angle, 0, 360, 255, -1)
    return new_image

def create_rectangle_image(image, x, y, w, h):
    new_image = np.zeros(image.shape, dtype=np.uint8)
    cv2.rectangle(new_image, (x, y), (x + w, y + h), 255, -1)
    return new_image

def main():
    img = np.zeros((512,512), np.uint8)
    #cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
    new_image = create_ellipse_image(img, 100, 50, 0, 256, 256)
    cv2.imshow('ellipse', new_image)

    rect_image = create_rectangle_image(img, 256, 256, 100, 100)
    cv2.imshow('rectangle', rect_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()