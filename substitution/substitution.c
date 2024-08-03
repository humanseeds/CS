#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    //validate that there is 1 command line argument
     if (argc != 2)
    {
      printf("Usage: ./substiution key\n");
      return = 1;
    }
    // assign the key a variable and make sure the key is 25 characters
    string key = argv[1]
    for (i =0; 1 < strlen(key)); i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Usage: ./substiution key\n");
            return = 1;
        }
    }

     if strlen(argv[]) != 26
        {
            printf("Key must contain 26 characters");
        }

}
