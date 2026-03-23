import cv2
import os
import numpy as np
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
image_file = os.path.join(script_dir, "img.jpg")
output_file = os.path.join(script_dir, "img_bright.jpg")
matrix_file = os.path.join(script_dir, "image_matrix.txt")
matrix_bright_file = os.path.join(script_dir, "image_matrix_bright.txt")

img = cv2.imread(image_file)

np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)
with open(matrix_file, "w", encoding="utf-8") as f:
    f.write(np.array2string(img, separator=', '))

image_matrix = img.tolist()

height = len(image_matrix)
width = len(image_matrix[0])
colors = len(image_matrix[0][0])
brightness = 100 # free to change

for y in range(height):
    for x in range(width):
        for c in range(colors):
            current_value = image_matrix[y][x][c]
            new_value = current_value + brightness
            
            if new_value > 255:
                new_value = 255
            elif new_value < 0:
                new_value = 0
            
            image_matrix[y][x][c] = new_value

img_baru = np.array(image_matrix, dtype=np.uint8)

with open(matrix_bright_file, "w", encoding="utf-8") as f:
    f.write(np.array2string(img_baru, separator=', '))

cv2.imwrite(output_file, img_baru)

print("Proses penulisan matriks dan penambahan brightness manual selesai!")