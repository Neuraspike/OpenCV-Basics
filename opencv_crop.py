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

# grab only elon musk body
elonBody = image[1:537, 65:256]
cv2.imshow("Elon Body", elonBody)
cv2.waitKey(0)

# grab only elon face
elonFace = image[3:80, 124:201]
cv2.imshow("Elon Face", elonFace)
cv2.waitKey(0)

# grab the tesla car
teslaCar = image[212:430, 227:825]
cv2.imshow("Tesla Car", teslaCar)

# waits for any key to be pressed then remove
# any created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()
