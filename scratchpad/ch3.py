import cv2
import numpy as np
from scipy import ndimage

# High pass filter.
#-------------------------------------------------------------------------------

# kernel_3x3 = np.array([[-1, -1, -1],
#                        [-1,  8, -1],
#                        [-1, -1, -1]])
#
# kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
#                        [-1,  1,  2,  1, -1],
#                        [-1,  2,  4,  2, -1],
#                        [-1,  1,  2,  1, -1],
#                        [-1, -1, -1, -1, -1]])
#
# img = cv2.imread('assets/baboon.jpg', cv2.IMREAD_GRAYSCALE)
#
# k3 = ndimage.convolve(img, kernel_3x3)
# k5 = ndimage.convolve(img, kernel_5x5)
# blurred = cv2.GaussianBlur(img, (17, 17), 0)
# g_hpf = img - blurred
#
# cv2.imshow('3x3', k3)
# cv2.imshow('5x5', k5)
# cv2.imshow('blurred', blurred)
# cv2.imshow('g_hpf', g_hpf)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Canny edge detection.
#-------------------------------------------------------------------------------

# img = cv2.imread('assets/baboon.jpg', 0)
#
# cv2.imwrite('output/canny.jpg', cv2.Canny(img, 200, 300))
# cv2.imshow('canny', cv2.imread('output/canny.jpg'))
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# Contour detection.
#-------------------------------------------------------------------------------

# Create a black image.
img = np.zeros((300, 300), dtype=np.uint8)

# Draw a square in two shades of gray.
img[50:150, 50:150] = 160
img[70:150, 60:160] = 128

# Apply a threshold so that the square becomes uniformly white.
ret, thresh = cv2.threshold(img, 127, 255, 0)

contours, hier = cv2.findContours(thresh, cv2.RETR_TREE,
                                  cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)

cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
