# HOW TO RUN
# python3 opencv_load_image_bonus.py --image images/floppy_disk.jpg --output output.jpg
# python3 opencv_load_image_bonus.py --image images/floppy_disk.jpg

# import the necessary modules
import argparse
import cv2

# initialize the argument parser and establish the arguments required
parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Path to the image')
parser.add_argument('--output', default='output.jpg', help='Path to the output image')
args = vars(parser.parse_args())

# load the image from where the file is located and get the
# spacial dimensions such as the width, height and #no of channels
image = cv2.imread(args['image'])

# grab and display the width, height and the #no of channels
# the loaded image currently has, in the terminal window
(h, w, c) = image.shape[:3]

print(f"Height: {h} pixels")
print(f"Width: {w} pixels")
print(f"No of channels: {c}")

# save the image directly to your current folder
cv2.imwrite(args['output'], image)

# display the image and waits for any key to be pressed
# then remove any created gui window from the screen & memory
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
