import os
from PIL import Image

def get_color_depth(image_path):
    img = Image.open(image_path)
    
    mode_to_bpp = {
        '1': 1,
        'L': 8,
        'P': 8,
        'RGB': 24,
        'RGBA': 32,
        'CMYK': 32,
        'YCbCr': 24,
        'I': 32,
        'F': 32
    }
    
    return mode_to_bpp.get(img.mode, "Format tidak dikenali")

script_dir = os.path.dirname(os.path.abspath(__file__))
image_file = os.path.join(script_dir, "img.jpg")
depth = get_color_depth(image_file)
print(f"Color Depth: {depth}-bit")