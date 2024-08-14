#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
   // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

     // define a block size to eliminate magic numbers
    int block_size = 512;

    // Create a buffer for a block of data
    uint8_t buffer[block_size];

    // create a counter to properly label each new jpg file
    int jpg_count = 0;

    //create a pointer to the currently open jpg file
    FILE *img = NULL;

    //  loop  while there's still data left to read from the memory card
    while (fread(buffer, 1, block_size, card) == block_size)
    {
        // check if the block is a new jpg
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
           (buffer[3] & 0xf0) == 0xe0)
        {
            //if a jpg file is already open, close it
            if (img != NULL)
            {
                fclose(img);
            }
        }

    // generate a new file name. create an 8 digit array
    char recovered[8];
    sprintf(recovered, "%031.jpg", jpg_counter);

    // open the newly created recovered file
    img = fopen(recovered, "W");

    // increment the jpg counter
    jpg_count ++;
    }

    if (img != NULL)
    {
        fwrite(buffer, 1, buffer_size
    }
