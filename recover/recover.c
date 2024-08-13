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

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // define a block size to eleminate magic numbers
    int block_size = 512

    // create a counter to properly label each new jpg file
    int file_count = 0;

    //create a pointer to the currently open jpg file
    FILE *img = NULL;
    // While there's still data left to read from the memory card
    while (fread(buffer, 1, block_size, card) == block_size)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&    // if first jpeg starts with certain jpg identifiers
           (buffer[3] & 0xf0) == 0xe0)
            {

                FILE *img = fopen(filename,"w" ); // create a new file for the found jpg
            }
            else int fclose(FILE *jpg; // if not the first jpg close the file and look for another
            {}
        }
        else // if a jpeg
            if // continue writing the next block of the jpg on the same file
    }
}
