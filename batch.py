# import os  # imports os module to get current directory information and allows us to change directory on demand
# import time  # imports time module to introduce delay in the program


# # Function to process each image
# def process_image(image_path):
#     # Add your image processing logic here
#     print(f"Processing image: {image_path}")

#     # creates a executable command with image-path to execute
#     command = f"python3 main.py --image={image_path} --img_size=320"
#     os.system(command)  # command is executed


# # Directory where images are located
# image_dir = "C:\\Users\\user\\Desktop\\HemathThakur\\Priority-Based-Parking-System\\input_images"

# # List all image files in the directory
# image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(".jpg")],
#                      key=lambda x: int(x.split("img")[1].split(".")[0]))
# # the directory is changed to the input_images and it identifies all the images with .jpg extension and sorts the images based on the name


# # Process each image sequentially
# for image_file in image_files:
#     image_path = os.path.join(image_dir, image_file)  # it changes the image name for each iteration
#     process_image(image_path)  # calls the command

#     # Add delay between processing each image
#     time.sleep(3)  # 3-second delay between each image processing


import os
import time

# Function to process each image
def process_image(image_path):
    print(f"Processing image: {image_path}")
    command = f"python main.py --image=\"{image_path}\" --img_size=320"
    os.system(command)

# Directory where images are located
image_dir = "C:\\Users\\user\\Desktop\\HemathThakur\\Priority-Based-Parking-System\\input_images"

# List all image files and filter valid ones
image_files = []
for f in os.listdir(image_dir):
    if f.endswith(".jpg") and "img" in f:
        try:
            num_part = f.split("img")[1].split(".")[0]
            if num_part.isdigit():  # Ensure it's a number
                image_files.append(f)
        except IndexError:
            print(f"Skipping invalid filename: {f}")

# Sort images based on their number
image_files = sorted(image_files, key=lambda x: int(x.replace(".jpg", "").replace("img", "")))

# Process each image sequentially
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    process_image(image_path)
    time.sleep(3)  # 3-second delay between each image processing
