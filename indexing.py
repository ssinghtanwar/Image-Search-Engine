# Importing ColorDescripter from colordescriptor.py
from colordescriptor import ColorDescripter
# Importing argparse for parsing the command line arguments
import argparse
# Importing Glob to Grab the file paths to images
import glob
# cv2 for OpenCV bindings
import cv2

# We’ll need two switches, --dataset , which is the path to our 
# photos directory, and --index which is the output CSV file 
# containing the image filename and the features associated 
# with each image.
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path of the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True, help = "Path to where the computed indexing will be stored")
args = vars(ap.parse_args())

# we initialize our ColorDescriptor using 8 Hue bins, 
# 12 Saturation bins, and 3 Value bins.
cd = ColorDescripter((8, 12, 3))

# Open the output index file for writing
output = open(args["index"], "w")

# Use glob to grab the image paths and loop over time
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    features = cd.describe(image)

    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))


output.close()



