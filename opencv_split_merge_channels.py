# HOW TO RUN
# python3 opencv_split_merge_channels.py --image images/rgb_circles.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# initialize the argument parser and establish the arguments required
parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Path to image')
args = vars(parser.parse_args())

# load the image and show it on screen
image = cv2.imread(args['image'])
cv2.imshow("Image", image)
cv2.waitKey(0)

# separate and visualize each color channels in respective order
(b, g, r) = cv2.split(image)

cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)
cv2.waitKey(0)

# merge the split image back together
mergedImage = cv2.merge([b, g, r])
cv2.imshow("Merged Image", mergedImage)
cv2.waitKey(0)

# visualize each color channels within single image
blank = np.zeros(image.shape[:2], dtype="uint8")

redChannel = cv2.merge([blank, blank, r])
cv2.imshow("Red", redChannel)

greenChannel = cv2.merge([blank, g, blank])
cv2.imshow("Green", greenChannel)

blueChannel = cv2.merge([b, blank, blank])
cv2.imshow("Blue", blueChannel)

# waits for any key to be pressed then remove any
# created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()
