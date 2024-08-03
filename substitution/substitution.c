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
      return 1;
    }

    // assign the key to a variable
    string key = argv[1];
    // check if the key is 26 characters long

    if (strlen(key) != 26)
    {
        printf("key must contain 26 characters\n");
        return 1;
    }

    // validate that the key is 26 alphabetical characters without duplicates
    for (int i =0; i < strlen(key); i++)
    {
        if (!isalpha(key[i]))
        {
            printf("key must contain 26 characters\n");
            return 1;
        }
    }

// validate the length of the key is 26 character
     if (strlen(key) != 26)
        {
            printf("Key must contain 26 characters.\n");
        }

// validate the key has no duplicate letters regardless of case
    for (int i = 0; i < strlen(key); i++)
    {
        for (int j = i + 1; j < strlen(key); j++)
        {
            if (toupper(key[i]) == toupper(key[j]))
            {
                printf("Usage: ./substiution key\n");
                return 1;
            }
        }
    }

//Prompt user for plaintext to cipher
string plaintext = get_string("plaintext: ");

// convert all characters in key to uppercase
for (int i = 0; 1 < strlen(key); i++)
{
    if(islower(key[i]))
    {
        key[i] = key[i] - 32;
    }
}

// print ciphertext
printf("ciphertext: ");

for (int i = 0; i < strlen(plaintext); i++)
  {
    if (isupper(plaintext[i]))
    {
        int letter = plaintext[i] - 65;
        printf("%c" , key[letter]);
    }
    else if (islower(plaintext[i]))
    {
        int letter = plaintext[i] -97;
        printf("%c" , key[letter] +32);
    }
    else printf("%c" , plaintext[i]);
  }
printf("\n");
}
