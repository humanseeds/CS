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





# this function converts the grayscale to asci chars
def gray_to_ascii(grayscale_image, ascii_chars= " .:;=+*%&@"):
    # get the size of the grayscale image
    width, height = grayscale_image.size

    # determine the number of ascii characters for the map
    char_len = len(ascii_chars)

    # create the ranges of pixel brightness to asign the ascii charcters to
    scale = 256 // char_len

    # create a list to store the accii version of each row
    ascii_art = []

    # loop through the height of the greyscale image
    for y in range(height):
        # create an empty string to reoresent the current row
        row = ""

        # loop over the columns of the grayscale image
        for x in range(width):
            # get the brightness of the pixel at the current location (x,y)
            brightness = grayscale_image.getpixel((x,y))
            # map the brightness of the pixel to the proper asci charcter
            row += ascii_chars[brightness // scale]
        # append the completed row of ascii charcters to the ascci_art list
        ascii_art.append(row)
    # combine all of the rows into a string, seperated by newline charcters
    return "\n".join(ascii_art)




def apply_filter(original_image_path, upload_folder):
    # create a copy of the original image.
    copied_image_path = copy_image(original_image_path, upload_folder)

    # convert the copied image to grayscale.
    grayscale_image = convert_to_grayscale(copied_image_path)

    # generate ascii art from the grayscale image.
    ascii_art = gray_to_ascii(grayscale_image)

    # save the grayscale image over the copied image.
    grayscale_image.save(copied_image_path)

    # return the ascii art and the path to the updated (grayscale) image.
    return ascii_art, copied_image_path
