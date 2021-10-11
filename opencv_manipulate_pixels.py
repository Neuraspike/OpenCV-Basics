# HOW TO RUN
# python3 opencv_manipulate_pixels.py --image images/elon_musk_tesla.png

# import the necessary modules
import argparse
import cv2

# initialize the argument parser and establish the arguments required
parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Path to the image')
parser.add_argument('--output', default='output.jpg', help='Path to the output image')
args = vars(parser.parse_args())

# load the image from disk and display it to the window
image = cv2.imread(args['image'])
cv2.imshow("Original", image)
cv2.waitKey(0)

# draw a rectangle on elon and tesla car
cv2.rectangle(image, (65, 1), (265, 537), (0, 255, 0), 2)  # elon musk
cv2.rectangle(image, (227, 212), (825, 430), (0, 255, 0), 2)  # tesla car

# add labels to the existing bounding boxes
cv2.putText(image, "Tesla Car", (825, 212), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2) # tesla label
cv2.putText(image, "Elon Musk", (269, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2) # elon label

# add some circles around his eyes and mouth
cv2.circle(image, (146, 38), 5, (0, 0, 255), 2)
cv2.circle(image, (165, 37), 5, (0, 0, 255), 2)
cv2.circle(image, (157, 60), 7, (0, 0, 255), 2)

# visualize the output
cv2.imshow("Output", image)
cv2.waitKey(0)
