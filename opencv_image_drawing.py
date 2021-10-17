# USAGE
# python3 opencv_image_drawing.py --image images/elon_musk_tesla.png

# import the necessary packages
import argparse
import cv2

# initialize the argument parser and establish the arguments required
parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True, help='Path to image')
args = vars(parser.parse_args())

# load the image specified in the command line
image = cv2.imread(args['image'])
cv2.imshow("Original", image)
cv2.waitKey(0)

# draw a rectangle on the image
cv2.rectangle(image, (65, 1), (265, 537), (0, 255, 0), 2)  # elon musk
cv2.rectangle(image, (227, 212), (825, 430), (0, 255, 0), 2)  # tesla car
cv2.imshow("Image - Added Rectangles", image)
cv2.waitKey(0)

# add a label to the tesla car and elon musk bounding box
image = cv2.putText(image, 'Elon Musk', (269, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 1)
image = cv2.putText(image, 'Tesla Car', (825, 212), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 1)
cv2.imshow("Image - Added Text", image)
cv2.waitKey(0)

# add circles to both his left and right eye along with his mouth
cv2.circle(image, (146, 38), 5, (0, 0, 255), 2)  # left eye
cv2.circle(image, (164, 36), 5, (0, 0, 255), 2)  # right eye
cv2.circle(image, (157, 60), 7, (0, 0, 255), 2)  # mouth
cv2.imshow("Image - Added Circles", image)
cv2.waitKey(0)

