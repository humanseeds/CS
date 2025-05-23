import math
import os
from PIL import Image, ImageFilter


# resize the image while keeping the same aspect ratio
def resize_image(image, new_width=100):
    # get the height and width of the image
    width, height = image.size

    # find the aspect ratio of the image
    ratio = height / width

    # set the new height to the aspect ratio of the width
    new_height = int(new_width * ratio)

    # resize the image to the new dimensions
    resized_image = image.resize((new_width, new_height))

    # return the resized image
    return resized_image


# this function converts the image to grayscale
# from here we can use the pixel intensity to apply asci charcters
def convert_to_grayscale(image):

    # convert to grayscale
    grayscale_image = image.convert("L")

    # return the grayscaled image
    return grayscale_image


# this function converts the grayscale to ascii chars
def gray_to_ascii(grayscale_image, ascii_chars=".,:;=*+%&@"):
    # get the size of the grayscale image
    width, height = grayscale_image.size

    # determine the number of ascii characters for the map
    char_len = len(ascii_chars)

    # create the ranges of pixel brightness to assign the ascii characters to
    scale = 256 // char_len

    # create a map to store the ascii strings that represent the pixels
    ascii_art = []

    # loop through the height of the greyscale image
    for y in range(height):
        row = ""
        for x in range(width):
            # set the brightness from the grayscale
            brightness = grayscale_image.getpixel((x, y))
            # ensure the brightness stays inbounds
            ascii_char = ascii_chars[min(brightness // scale, char_len - 1)]

            row += ascii_char

        ascii_art.append(row)
    return "\n".join(ascii_art)


# this function saves the final ascii rendition
def save_ascii(ascii_art, original_image_path, upload_folder):
    # create a file for the ascii art based on the original image
    ascii_filename = f"ascii_{os.path.basename(original_image_path)}.txt"

    # create a path to the file
    ascii_file_path = os.path.join(upload_folder, ascii_filename)

    # open the file with write mode and save the ascii art
    with open(ascii_file_path, "w") as file:
        file.write(ascii_art)

    # return the path of the saved ascii text file
    return ascii_file_path


# this function pulls all of the prious functions together to create the asci art
def process_image(image_path, upload_folder, new_width):
    # fetch the image
    image = Image.open(image_path)

    # resize the image
    resized_image = resize_image(image, new_width)

    # convert the image to grayscale
    grayscale_image = convert_to_grayscale(resized_image)

    # generate the ascii art from the grayscaled image
    ascii_art = gray_to_ascii(grayscale_image)

    # save the ascii art to a text file
    ascii_file_path = save_ascii(ascii_art, image_path, upload_folder)

    # return the ascii art final path
    return ascii_art, ascii_file_path
