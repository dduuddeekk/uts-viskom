import os
import cv2
import numpy as np
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
image_file = os.path.join(script_dir, "img.jpg")
output_file = os.path.join(script_dir, "color.txt")

img = cv2.imread(image_file)

np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(np.array2string(img, separator=', '))