import numpy as np
import cv2
from mss import mss
from PIL import Image


b_width = 300
b_height = 600
scaling_factor = 3

bounding_box = {'top': 100, 'left': 0, 'width': b_width, 'height': b_height}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)

    arr = np.array(sct_img)

    resize_down = cv2.resize(arr, ((b_width // scaling_factor), b_height), interpolation= cv2.INTER_LINEAR)


#    imshow_arr = np.mean(arr.reshape(-1, scaling_factor), axis=1).reshape(b_height, (b_width // scaling_factor), 4)

    cv2.imshow('screen', resize_down)
#    cv2.imshow('screen', arr)

#    print(arr.shape)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
