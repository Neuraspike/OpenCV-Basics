# HOW TO RUN
# python3 opencv_rotate.py --image images/elon_musk_tesla.png
# python3 opencv_rotate.py --image images/black_panther.jpeg

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

# grab the height and width and then compute the center of the image
(h, w) = image.shape[:2]
cX, cY = (w // 2, h // 2)

# rotate the image by 90 degrees (counter clock wise)
# around the center of the image
M = cv2.getRotationMatrix2D(center=(cX, cY),
                            angle=90,
                            scale=1.0)
rotatedImage = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Image Rotated by 90 degrees", rotatedImage)
cv2.waitKey(0)

# rotate the image by 65 degrees (clock wise)
# around the center of the image
M = cv2.getRotationMatrix2D(center=(cX, cY),
                            angle=-65,
                            scale=1.0)
rotatedImage = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Image Rotated by 65 degrees", rotatedImage)
cv2.waitKey(0)

# rotate the image by 65 degrees (anti clock-wise) from (50,50)
M = cv2.getRotationMatrix2D(center=(50, 50),
                            angle=65,
                            scale=1.0)

print(f"Rotation Matrix:\n   {M}")

rotatedImage = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Image Rotated by 65 degrees from (50,50) ", rotatedImage)
cv2.waitKey(0)


def rotate_image(image, angle):
    # get with dimension of the image and then compute the center
    (h, w) = image.shape[:2]  # note numpy uses (y,x)
    (cX, cY) = (w // 2, h // 2)

    # get the rotation matrix, then extract the sine and cosine
    # value within the rotation matrix (Opencv func uses (x,y))
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cosine = np.abs(M[0, 0])
    sine = np.abs(M[0, 1])

    # compute the new image size
    new_width = int((h * sine) + (w * cosine))
    new_height = int((h * cosine) + (w * sine))

    # Located the translation that moves the image to the center of the
    # image and then updated the translation part of the rotation matrix
    M[0, 2] += (new_width / 2) - cX
    M[1, 2] += (new_height / 2) - cY


    # perform the proper rotation of the image and then return the image
    image = cv2.warpAffine(image, M, (new_width, new_height))

    return image


# rotate an image 65 degrees clockwise
rotatedImage = rotate_image(image, -65)
cv2.imshow("Image Rotated by 65 degree", rotatedImage)
cv2.waitKey(0)

# rotate an image 90 degrees anti-clockwise
rotatedImage = rotate_image(image, 90)
cv2.imshow("Image Rotated by 90 degree", rotatedImage)

# waits for any key to be pressed then remove any
# created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()
