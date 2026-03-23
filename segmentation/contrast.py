import cv2
import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
image_file = os.path.join(script_dir, "img.jpg")
output_file = os.path.join(script_dir, "img_contrast.jpg")
# matrix_file = os.path.join(script_dir, "image_matrix.txt")
matrix_contrast_file = os.path.join(script_dir, "image_matrix_contrast.txt")

img = cv2.imread(image_file)
image_matrix = img.tolist()

height = len(image_matrix)
width = len(image_matrix[0])
colors = len(image_matrix[0][0])

alpha = 1.5 # factor to change (greater than 1 increases contrast, between 0 and 1 decreases contrast)
brightness_adj = 0

for y in range(height):
    for x in range(width):
        for c in range(colors):
            current_value = image_matrix[y][x][c]
            
            new_value = alpha * (current_value - 128) + 128 + brightness_adj
            
            if new_value > 255:
                new_value = 255
            elif new_value < 0:
                new_value = 0
            
            image_matrix[y][x][c] = int(new_value)
            
img_baru = np.array(image_matrix, dtype=np.uint8)

with open(matrix_contrast_file, "w", encoding="utf-8") as f:
    f.write(np.array2string(img_baru, separator=', '))

cv2.imwrite(output_file, img_baru)

print(f"Proses kontras manual (Alpha: {alpha}) selesai!")