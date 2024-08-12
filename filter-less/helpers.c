#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all pixels in height
    for (int i = 0; i < height; i++)
    {
        // loop over all pixels in width
        for (int j = 0; j < width; j++)
        {

            // average out the three pixel types
            int average =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            // assign the average to the pixels in the array
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// create a helper function to ensure rgbt values dont exceed 255
int capped255(int value)
{
    if (value > 255)
    {
        return 255;
    }
    else
    {
        return value;
    }
}
// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all pixels in height and width
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // apply the sepia algorithm to each RGB portion of the pixel
            int sepiaRed = round((.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) +
                                 (.189 * image[i][j].rgbtBlue));
            int sepiaGreen = round((.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) +
                                   (.168 * image[i][j].rgbtBlue));
            int sepiaBlue = round((.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) +
                                  (.131 * image[i][j].rgbtBlue));

            // recall helper function to ensure the new value does now exceed the 255 max limit
            sepiaRed = capped255(sepiaRed);
            sepiaGreen = capped255(sepiaGreen);
            sepiaBlue = capped255(sepiaBlue);

            // apply the new calculated sepia filter
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // loop throught the pixels
    for (int i = 0; i < height; i++)
    {
        // for width we only need to loop through half the pixels because they are swaped with the
        // other half
        for (int j = 0; j < width / 2; j++)
        {
            // calculate where the opposite pixel on the row is
            int oppositePixel = width - j - 1;

            // swap the pixels using a temporary variable
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][oppositePixel];
            image[i][oppositePixel] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create a copy of the image by looping through the width and height
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // loop through each pixel of the original
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // initialize variables of the pixels to zero and create a counter to find averages
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            int counter = 0;

            // now we must loop through a 3 x 3 grid around each pixel
            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    // determine the cooridnates of the current neighbor pixels
                    int currentX = i + x;
                    int currentY = j + y;

                    // check to see if the neighboring pixel is in bounds and not out of the array
                    if (currentX >= 0 && currentX < width && currentY >= 0 && currentY < height)
                    {
                        // now we find the sums of the neighbor pixels color values
                        sumRed += copy[currentX][currentY].rgbtRed;
                        sumGreen += copy[currentX][currentY].rgbtGreen;
                        sumBlue += copy[currentX][currentY].rgbtBlue;
                        counter++;
                    }
                }
            }
            // now we find the average of the pixels and again cap the value with our helper
            // function
            image[i][j].rgbtRed = capped255(round((float) sumRed / counter));
            image[i][j].rgbtGreen = capped255(round((float) sumGreen / counter));
            image[i][j].rgbtBlue = capped255(round((float) sumBlue / counter));
        }
    }

    return;
}
