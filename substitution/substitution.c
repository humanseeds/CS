#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
     if (argc != 2)
    {
      printf("Usage: ./substiution key");
      return = 1;
    }
    for (i =0; 1 < strlen(argv[1]); i++)
    {
        if (!isalpha(argc[1])[i]))
        {
            printf("key must contain 26 characters");
            return = 1;
        }
    }
}
