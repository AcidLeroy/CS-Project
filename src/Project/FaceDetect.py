# Import numpy
import numpy as np

# Import Thunder
from pyspark import SparkContext, SparkConf
from thunder import Colorize, ThunderContext
image = Colorize.image

# Import opencv
import cv2
import sys

# Use OpenCV2 haar cascade to detect face and display it for 1 sec
def convertToGray(cur_img):
    gray = cv2.cvtColor(cur_img, cv2.COLOR_BGR2GRAY)
    return gray

def detectFaces(img):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier('/home/vj/Desktop/CS-Project/src/Tutorials/haarcascade_frontalface_default.xml')

    # Show img when converted to unsigned integer

    img = np.uint8(img*255) #!!!! BAD CODE, NEED TO FIX THIS

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        img,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), -1)
    return img


# Load images using thundear and pass it to OpenCV haar cascase one by one
if __name__ == '__main__':
    # Define Spark and Thunder context
    conf = SparkConf() \
        .setAppName("Collaborative Filter") \
        .set("spark.executor.memory", "5g")
    sc = SparkContext(conf=conf)
    tsc = ThunderContext(sc)

    # Load all images in data directory
    data = tsc.loadImages('/home/vj/Desktop/CS-Project/data',inputFormat='png')

    # Loop through each image and convert them to gray
    grayImages = data.apply(lambda (k,v): (k,convertToGray(v)))

    # Loop through all the gray images and find faces
    FaceImages = grayImages.apply(lambda (k,v): (k,detectFaces(v)))
    print(data.dims)
    print(data.nrecords)
    cv2.imshow('image1',grayImages[0])
    cv2.imshow('Face detected1',FaceImages[0])
    cv2.imshow('image2',grayImages[1])
    cv2.imshow('Face detected2',FaceImages[1])
    cv2.imshow('image3',grayImages[2])
    cv2.imshow('Face detected3',FaceImages[2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #
