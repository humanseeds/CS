#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all pixels in height
    for (int i = 0; i < height; i ++)
    {
        // loop over all pixels in width
        for (int j = 0; j < width; j ++)
        {

         //average out the three pixel types
          int average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

          //assign the average to the pixels in the array
          image[i][j].rgbtRed = average;
          image[i][j].rgbtgreen = average;
          image[i][j].rgbtblue = average;
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
            int sepiaRed = round((.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue));
            int sepiaGreen = round((.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue));
            int sepiaBlue = round((.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue));

            // recall helper function to ensure the new value does now exceed the 255 max limit
            sepiaRed = capped255(sepiaRed);
            sepiaGreen = capped255(sepiaGreen);
            sepiaBlue = capped255(sepiaBlue);

            // apply the new calculated sepia filter
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = SepiaBlue;

        }
    }


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
