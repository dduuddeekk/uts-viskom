import os
import exiftool

script_dir = os.path.dirname(os.path.abspath(__file__))
image_file = os.path.join(script_dir, "img.jpg")
output_file = os.path.join(script_dir, "metadata.txt")

exiftool_path = r"C:\exiftool\exiftool-13.53_64\exiftool(-k).exe"

with exiftool.ExifToolHelper(executable=exiftool_path) as et:
    metadata = et.get_metadata(image_file)
    
    with open(output_file, "w", encoding="utf-8") as f:
        for d in metadata:
            f.write("METADATA:\n")
            for key, value in d.items():
                f.write(f"{key:35}: {value}\n")