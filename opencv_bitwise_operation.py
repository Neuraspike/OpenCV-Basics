# import the necessary packages
import numpy as np
import cv2

# draw a square
square = np.zeros((200, 200), dtype='uint8')
cv2.rectangle(square, (15, 15), (185, 185), 255, -1)
cv2.imshow("Square", square)
cv2.waitKey(0)

# draw a circle
circle = np.zeros((200, 200), dtype='uint8')
cv2.circle(circle, (100, 100), 95, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# The bitwise and operation is only true,
# when both inputs haves a value that is 'ON'.
# which means if the pixel haves are greater than zero
bitwiseAnd = cv2.bitwise_and(square, circle)
cv2.imshow("Bitwise Operation - AND", bitwiseAnd)
cv2.waitKey(0)

# If either pixel values are greater than zero
bitwiseOr = cv2.bitwise_or(square, circle)
cv2.imshow("Bitwise Operation - OR", bitwiseOr)
cv2.waitKey(0)

# Quite similar to the OR statement only with a single
# condition, that both pixels are not allowed to have
# pixel values of 255
bitwiseXor = cv2.bitwise_xor(square, circle)
cv2.imshow("Bitwise Operation - XOR", bitwiseXor)
cv2.waitKey(0)

# inverts the pixel values; pixel values of 0 becomes 255;
# pixel values of 255 becomes 0
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("Bitwise Operation - NOT", bitwiseNot)

# waits for any key to be pressed then remove any
# created gui window from the screen & memory
cv2.waitKey(0)
cv2.destroyAllWindows()
