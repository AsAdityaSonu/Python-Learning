import numpy as np
import matplotlib.pyplot as plt

def load_and_display_image_from_txt(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    data = list(map(int, data.split()))
    total_elements = len(data)

    num_channels = 3

    if total_elements % num_channels != 0:
        raise ValueError("Total number of elements is not divisible by 3, cannot form an RGB image.")

    num_pixels = total_elements // num_channels

    image_height = int(np.sqrt(num_pixels))
    image_width = num_pixels // image_height

    while image_height * image_width * num_channels != total_elements:
        image_height -= 1
        image_width = num_pixels // image_height

    image_array = np.array(data).reshape((image_height, image_width, num_channels))

    plt.imshow(image_array)
    plt.axis('off') 
    plt.show()

load_and_display_image_from_txt("imageRGB.txt")  
