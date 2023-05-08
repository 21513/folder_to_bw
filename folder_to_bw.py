from PIL import Image
import os

# Set the path to the folder containing the images
path = ""

# Get a list of all files in the folder
files = os.listdir(path)

# Loop through each file in the folder
for file in files:
    # Check if the file is an image
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        # Open the image and convert it to black and white
        with Image.open(os.path.join(path, file)) as img:
            bw_img = img.convert("L")
            # Save the black and white image
            bw_img.save(os.path.join(path, "" + file))
