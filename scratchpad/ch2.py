import cv2
import numpy as np
import os

# Construct image.
#-------------------------------------------------------------------------------

# img = np.zeros((5, 3), dtype=np.uint8)
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#
# print(img)
# print(img.shape)

# Convert image.
#-------------------------------------------------------------------------------

# img = cv2.imread('assets/graf3.png')
# cv2.imwrite('output/graf3.jpg', img)

# Convert image to grayscale.
#-------------------------------------------------------------------------------

# img = cv2.imread('assets/graf3.png', cv2.IMREAD_GRAYSCALE)
# cv2.imwrite('output/graf3.jpg', img)

# Convert random bytes into grayscale and BGR images.
#-------------------------------------------------------------------------------

# random_byte_array = bytearray(os.urandom(120000))
# np_array = np.array(random_byte_array)
#
# img_gray = np_array.reshape(300, 400)
# cv2.imwrite('output/gray_noise.png', img_gray)
#
# img_color = np_array.reshape(100, 400, 3)
# cv2.imwrite('output/color_noise.png', img_color)

# Maximize image blue channel.
#-------------------------------------------------------------------------------

# img = cv2.imread('assets/lena.jpg')
# img[:, :, 0] = 255
# cv2.imwrite('output/blue_lena.jpg', img)

# Operate on region of interest.
#-------------------------------------------------------------------------------

# img = cv2.imread('assets/lena.jpg')
# print(img.shape)
# print(img.size)
# print(img.dtype)
# img[128:384, 128:384, 0] = 255
# cv2.imwrite('output/roi_lena.jpg', img)

# Convert video format.
#-------------------------------------------------------------------------------

# vidcap = cv2.VideoCapture('assets/Megamind.avi')
# fps = vidcap.get(cv2.CAP_PROP_FPS)
# size = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# writer = cv2.VideoWriter(
#     'output/MegamindOutput.mkv',
#     cv2.VideoWriter_fourcc(*'avc1'),
#     fps,
#     size)
#
# success, frame = vidcap.read()
# while success:
#     writer.write(frame)
#     success, frame = vidcap.read()

# Capture video frames.
#-------------------------------------------------------------------------------

# capture = cv2.VideoCapture(0)
# fps = capture.get(cv2.CAP_PROP_FPS)
# size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# writer = cv2.VideoWriter(
#     'output/camera_capture.mkv',
#     cv2.VideoWriter_fourcc(*'avc1'),
#     fps,
#     size)
#
# success, frame = capture.read()
# num_frames_remaining = 10 * fps - 1
#
# while success and num_frames_remaining > 0:
#     writer.write(frame)
#     success, frame = capture.read()
#     num_frames_remaining -= 1

# Display an image.
#-------------------------------------------------------------------------------

# img = cv2.imread('assets/lena.jpg')
# cv2.imshow('hello lena', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Display camera frames.
#-------------------------------------------------------------------------------

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

windowName = 'display camera frames'

capture = cv2.VideoCapture(0)
cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, onMouse)

success, frame = capture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow(windowName, frame)
    success, frame = capture.read()

cv2.destroyWindow(windowName)
capture.release()



