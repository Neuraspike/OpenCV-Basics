# HOW TO RUN
# python3 opencv_flip.py --image images/opencv_logo.png

# import the necessary packages
import argparse
import cv2

# initialize the argument parser and establish the arguments required
parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Path to image')
args = vars(parser.parse_args())

# load the image and show it on screen
image = cv2.imread(args['image'])
cv2.imshow("Image", image)

# flip the image horizontally
flippedImage = cv2.flip(image, 1)
cv2.imshow("Horizontal image", flippedImage)
print(f"[INFO] flipping image horizontally...")
cv2.waitKey(0)

# flip the image vertically
flippedImage = cv2.flip(image, 0)
cv2.imshow("Vertical Image", flippedImage)
print(f"[INFO] flipping image vertically...")
cv2.waitKey(0)

# flip the image both horizontally and vertically
flippedImage = cv2.flip(image, -1)
cv2.imshow("Horizontal and Vertical flip", flippedImage)
print(f"[INFO] flipping image horizontally and then vertically...")

# waits for any key to be pressed then remove any
# created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()
