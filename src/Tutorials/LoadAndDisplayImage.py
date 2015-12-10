# Load thunder
from pyspark import SparkContext, SparkConf
from thunder import Colorize, ThunderContext
image = Colorize.image
import os

#Load Sci-kit image
from skimage.viewer import ImageViewer as skImageViewer

#Load spark context
conf = SparkConf() \
    .setAppName("Display face") \
    .set("spark.executor.memory", "5g")
sc = SparkContext(conf=conf)
#load thunder bolt context
tsc = ThunderContext(sc)

# Load image using thunder
data = tsc.loadImages(os.path.dirname(os.path.realpath(__file__))+'/mush.png',inputFormat='png')
img  = data.first()[1]

# Display image using Sci-kit image
viewer = skImageViewer(img[:,:,0])
viewer.show()
