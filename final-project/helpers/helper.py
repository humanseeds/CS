import math
import os
from PIL import Image, ImageFilter


#function to create a copy of the original uploaded image to augment with filters

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


# this function converts the grayscale to asci chars
def gray_to_ascii(grayscale_image, ascii_chars= " .:;=+*%&@"):
    width, height = grayscale_image.size

    char_len = len(ascii_chars)
    scale = 256 // char_len

    ascii_art = []

    for y in range(height):
        row = ""
        for x in range(width):
            brightness = grayscale_image.getpixel((x,y))
            row += ascii_chars[brightness // scale]
        ascii_art.append(row)
    return "|n".join(ascii_art)


def apply_filter(image_path):

    image = Image.open(image_path)
    image_copy = image.copy()
    grayscale_image = convert_to_grayscale(image.path)
    ascii_art = gray_to_ascii(grayscale_image)
    filtered_image_path = os.path.join(app.config['UPLOAD_FOLDER'],"filtered_' + os.path.basename(image_path))
    grayscale_image.save(filtered_image)

    return ascii_art, filtered_image
