# HOW TO RUN
# python3 opencv_resize.py --image images/tony_stark.jpg
# python3 opencv_resize.py --image images/n_for_neuraspike.png

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
cv2.waitKey(0)

# resize the image to be 600 pixels wide by calculating the
# ratio of the new width compared to the old width
ratio = 600.0 / image.shape[1]
dimension = (600, int(image.shape[0] * ratio))

# resize the original image
resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image - Width", resizedImage)
cv2.waitKey(0)

# resize the image to have a height of 400 pixels
ratio = 400.0 / image.shape[0]
dimension = (int(image.shape[1] * ratio), 400)

# perform the resizing and waits for any key to be pressed
resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized image - Height", resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    # check if the width and height is specified
    if width is None and height is None:
        return image

    # initialize the dimension of the image and grab the
    # width and height of the iamge
    dimension = None
    (h, w) = image.shape[:2]

    # calculate the ratio of the height and
    # construct the new dimension
    if height is not None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))

    # resize the image
    resizedImage = cv2.resize(image, dimension, interpolation=inter)

    return resizedImage


# initialize different interpolation methods
interpolation_methods = [
    ["cv2.INTER_NEAREST", cv2.INTER_NEAREST],
    ["cv2.INTER_LINEAR", cv2.INTER_LINEAR],
    ["cv2.INTER_AREA", cv2.INTER_AREA],
    ["cv2.INTER_CUBIC", cv2.INTER_CUBIC],
    ["cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4]
]

# iterate over different interpolation methods
for (inter_name, method) in interpolation_methods:
    resizedImage = resize_image(image, width=image.shape[1] * 4, inter=method)
    cv2.imshow(f"{inter_name}", resizedImage)
    print(f"[INFO] Interpolation method: {inter_name}")
    cv2.waitKey(0)

cv2.destroyAllWindows()
