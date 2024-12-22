import math
import os
from PIL import Image, ImageFilter






def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    return grayscale_image


def apply_sobel(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    sobel_image = grayscale_image.filter(ImageFilter.Find_EDGES)
    return sobel_image

