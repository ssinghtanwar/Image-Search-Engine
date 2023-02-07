from colordescriptor import ColorDescripter
from searcher import Searcher
import argparse
import cv2

# Constructing Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True, help = "Path to where the computed index is stored")
ap.add_argument("-q", "--query", required = True, help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True, help = "Path to the result path")
args = vars(ap.parse_args())

# initializing image descriptor
cd = ColorDescripter((8, 12, 3))

# Load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# Perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# Loop over results
for (score, resultID) in results:
    # load the result image
    result = cv2.imread(args["result_path"] + "/" + resultID)

    # Display the Result image
    cv2.imshow("Result", result)
    cv2.waitKey(0)