# Face Obsucration Using Big Data Techniques

In this paper we investigate some of the techniques that are used
for face recognition so that we can find the faces in sensitive data,
and automatically blur them to anonymize the people in the videos.
This is an effort to aid the UNM school of engineering's project,
"Advancing out of school learning in mathematics and engineering"
or AOLME. This approach is by no means novel, but is more of
an investigation of applying computer vision algorithms at a
"big-data" scale.

##Tutorials
###Face detection using {opencv2}
$python2 cv2face_detect.py little_mix_wrong.jpg haarcascade_frontalface_default.xml

###Face recognition using {skikit-learn}
python2 SciKitLearn_face_recognition.py

###Loading and displaying image using {thunder} and {Scikit-image}
thunder LoadAndDisplayImage.py
###Loading and displaing image using {thudner} and {OpenCV2}
thunder src/Tutorials/ThunderCv2.py

##Project
###Face detection
thunder src/Project/FaceDetect.py
 -) Please go through the code and change the directory. The images
    need to be in 'png' format to be loaded.
