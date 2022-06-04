# HOW TO RUN
# python3 opencv_flip.py --image images/lucid.jpg

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
horizontal_flip_img = cv2.flip(image, flipCode=1)
cv2.imshow("Horizontal flip", horizontal_flip_img)
print(f"[INFO] flipping image horizontally...")
cv2.waitKey(0)

# flip the image vertically
vertical_flip_img = cv2.flip(image, flipCode=0)
cv2.imshow("Vertical flip", vertical_flip_img)
print(f"[INFO] flipping image vertically...")
cv2.waitKey(0)

# flip the image both horizontally and vertically
flip_image = cv2.flip(image, flipCode=-1)
cv2.imshow("Horizontal and vertical flip", flip_image)
print(f"[INFO] flipping image horizontally and then vertically...")

# waits for any key to be pressed then remove any
# created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()