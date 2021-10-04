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


def load_image(filename):
    """
    :param filename: path to the image file
    :return: a numpy array if the image file exists
             else None
    """
    image = cv2.imread(filename)

    # validate if the image was loaded correctly
    if image is None:
        return None

    return image


# load the image from where the file is located
image = load_image(args['image'])

# validate if the image was loaded properly
if image is None:
    print("Do nothing")
else:
    # display the image and waits for any key to be pressed;
    # remove any created gui window from the screen & memory;
    # and then save the image directly to your current folder
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.imwrite(args['output'], image)
