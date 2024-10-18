import numpy as np
from PIL import Image

def imgToArray(path):
    image = Image.open(path)
    imageArray = np.array(image)
    
    if len(imageArray.shape) == 3:
        np.savetxt("imageRGB.txt", imageArray.reshape(-1, imageArray.shape[2]), fmt='%d')
        print("Image saved as RGB text file: imageRGB.txt")
    elif len(imageArray.shape) == 2:  
        np.savetxt("imageGreyscale.txt", imageArray, fmt='%d')
        print("Image saved - Greyscale text file: imageGreyscale.txt")
    else:
        print("Unknown image format")

imgToArray("ML Assignments/Assignment 1/linux.jpg")


