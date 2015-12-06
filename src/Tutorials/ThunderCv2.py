# Load thunder
from pyspark import SparkContext, SparkConf
from thunder import Colorize, ThunderContext
image = Colorize.image

# Load OpenCV2
import cv2

#Load spark context
conf = SparkConf() \
    .setAppName("Collaborative Filter") \
    .set("spark.executor.memory", "5g")
sc = SparkContext(conf=conf)
#load thunder bolt context
tsc = ThunderContext(sc)

# Load image using thunder
data = tsc.loadImages('/home/vj/Desktop/CS-Project/src/Tutorials/mush.png',inputFormat='png')
img  = data.first()[1]

# Display image using OpenCV2
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
