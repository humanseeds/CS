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

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        int i = 0; i < 512 ; i++; // not sure what to run as the end of the file
        // Create JPEGs from the data
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&    // if first jpeg starts with certain jpg identifiers
           (buffer[3] & 0xf0) == 0xe0)
            {
                sprintf(filename, "%03i.jpg",x ); // store the new file in memory until a full jpg is found
                FILE *img = fopen(filename,"w" ); // create a new file for the found jpg
            }

        }
    }
}
