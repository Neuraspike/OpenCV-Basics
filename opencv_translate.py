# HOW TO RUN
# python3 opencv_translate.py --image images/emirates_plane.jpg

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

# grab the height and width of the image
(h, w) = image.shape[:2]

# shift the image 150 pixels to the right and 50 pixels down
# then display the result to the image
M = np.float32([[1, 0, 150],
                [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted right and down", shifted)
cv2.waitKey(0)

# shift the image 150 pixels to the left and
# 50 pixels upwards then display the result

M = np.float32([[1, 0, -150],  # 1,0, shiftX
                [0, 1, -50]])  # 0,1, shiftY
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted left and up", shifted)

# waits for any key to be pressed then remove
# any created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()
