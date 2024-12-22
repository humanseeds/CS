import math
import os
from PIL import Image, ImageFilter

#resize the image while keep the same aspect ratio
def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image



# this function converts the image to grayscale
# from here we can use the pixel intensity to apply asci charcters
def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    return grayscale_image


# this function applies the sobel operator for edge detection and direction
# this will give our edges more definition
def apply_sobel(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    sobel_image = grayscale_image.filter(ImageFilter.Find_EDGES)
    return sobel_image


# this function converts the grayscale to asci charctera
def Gray_to_ascii(grayscale_image, ascii_chars= " .:;=+*%&@"):
    width, height =grayscale_image.size

    char_len = len(ascii_chars)
    scale = 256 // char_len

    ascci_art = []
    for y in range(grayscale_image.height):
        row
