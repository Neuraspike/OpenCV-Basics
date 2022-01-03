# HOW TO RUN
# python3 opencv_masking.py --image images/elon_musk_tesla.png

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

# generate a rectangular mask which has two pixels values (0 & 255).
# and once applied to an image, pixels values with 255 (foreground) will be
# preserved and values with 0  will be overlooked
rectangularMask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(rectangularMask, (65, 1), (256, 537), 255, -1)
cv2.imshow("Rectangular Mask", rectangularMask)

# apply the rectangular mask and notice how the elon's body is preserved
bodyMasked = cv2.bitwise_and(image, image, mask=rectangularMask)
cv2.imshow("Mask Applied to Body", bodyMasked)
cv2.waitKey(0)

# generate a circular mask with a radius of 50 and apply the mask again
circularMask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(circularMask, (160, 54), 50, 255, -1)
faceMasked = cv2.bitwise_and(image, image, mask=circularMask)

# show the output and waits for any key to be pressed
# then remove any created gui window from the screen & memory
cv2.imshow("Circular Mask", circularMask)
cv2.imshow("Mask Applied to Face", faceMasked)
cv2.waitKey(0)
cv2.destroyAllWindows()

