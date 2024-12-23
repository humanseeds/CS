import math
import os
from PIL import Image, ImageFilter


# function to create a copy of the original uploaded image to augment with filters
def copy_image(image_path, upload_folder):
    # open the original image
    original_image = Image.open(image_path)

    # create a path for the copied image
    copy_image_path = os.path.join(upload_folder, 'copy_' + os.path.basename(image_path))

    # save the copy of the image
    original_image.save(copy_image_path)

    # return athe path to the copied image
    return copy_image_path




# resize the image while keep the same aspect ratio
def resize_image(image, new_width):
    # get the hieght and width of the image
    width, height = image.size

    # find the aspect ratio of the image
    ratio = height / width

    # set the new hieght to the aspect ratio of the width
    new_height = int(new_width * ratio)

    # resize the image to the new dimensions
    resized_image = image.resize((new_width, new_height))

    # return the resized image
    return resized_image




# this function converts the image to grayscale
# from here we can use the pixel intensity to apply asci charcters
def convert_to_grayscale(image_path):
    # open the image
    image = Image.open(image_path)

    # convert to grayscale
    grayscale_image = image.convert("L")

    # return the grayscaled image
    return grayscale_image




# this function applies the sobel operator for edge detection and direction
# this will give our edges more definition
def apply_sobel(image_path):
    # open the image
    image = Image.open(image_path)
    #
    grayscale_image = image.convert("L")

    sobel_image = grayscale_image.filter(ImageFilter.Find_EDGES)

    # return the sober image
    return sobel_image




# this function converts the grayscale to asci chars
def gray_to_ascii(grayscale_image, ascii_chars= " .:;=+*%&@"):
    # get the size of the grayscale image
    width, height = grayscale_image.size

    # asign the length of the asci character string
    char_len = len(ascii_chars)

    # create the ranges of pixel brightness to asign the asci charcters to
    scale = 256 // char_len

    # create a 
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

    grayscale_image = convert_to_grayscale(image.path)
    ascii_art = gray_to_ascii(grayscale_image)
    filtered_image_path = os.path.join(app.config['UPLOAD_FOLDER'],"filtered_' + os.path.basename(image_path))
    grayscale_image.save(filtered_image)

    return ascii_art, filtered_image
