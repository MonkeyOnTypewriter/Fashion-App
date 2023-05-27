from PIL import Image
import os

folder_path = 'bags'
n = 0

def convert_to_jpg(input_file, output_file):
    try:
        image = Image.open(input_file)
        image.save(output_file, "JPEG")
        return 0
    except IOError as e:
        return 1

os.makedirs('jpgs', exist_ok=True)


for i, file_name in enumerate(os.listdir(folder_path)):
    input_file_path = os.path.join(folder_path, file_name)
    output_file_path = f"jpgs/{i}.jpg"  # Update with the desired path for the output JPG file
    n = n + convert_to_jpg(input_file_path, output_file_path)

print(f'failures = {n}')