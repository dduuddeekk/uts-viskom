import cv2
import os
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
image_file = os.path.join(script_dir, "img.jpg")
output_file = os.path.join(script_dir, "img_scaling.jpg")
# matrix_file = os.path.join(script_dir, "image_matrix.txt")
matrix_scale_file = os.path.join(script_dir, "image_matrix_scaling.txt")

img = cv2.imread(image_file)
orig_matrix = img.tolist()

orig_h = len(orig_matrix)
orig_w = len(orig_matrix[0])
colors = len(orig_matrix[0][0])

scale_x = 1.5 # free to change
scale_y = 1.5 # free to change

new_h = int(orig_h * scale_y)
new_w = int(orig_w * scale_x)

scaled_matrix = [[[0 for _ in range(colors)] for _ in range(new_w)] for _ in range(new_h)]

print(f"Scaling dari {orig_w}x{orig_h} menjadi {new_w}x{new_h}...")

for y_new in range(new_h):
    for x_new in range(new_w):
        
        x_orig = int(x_new / scale_x)
        y_orig = int(y_new / scale_y)
        
        if x_orig >= orig_w: x_orig = orig_w - 1
        if y_orig >= orig_h: y_orig = orig_h - 1
        
        for c in range(colors):
            scaled_matrix[y_new][x_new][c] = orig_matrix[y_orig][x_orig][c]

img_baru = np.array(scaled_matrix, dtype=np.uint8)
with open(matrix_scale_file, "w", encoding="utf-8") as f:
    f.write(np.array2string(img_baru, separator=', '))
cv2.imwrite(output_file, img_baru)
print(f"Proses scaling manual (Scale X: {scale_x}, Scale Y: {scale_y}) selesai!")