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
    for (int i = 0; i < strlen(key); i++)
    {
        if (!isalpha(key[i]))
        {
            printf("key must only contain alphabetic characters\n");
            return 1;
        }

        for (int j = i + 1; j < strlen(key); j++)
        {
            if (toupper(key[i]) == toupper(key[j]))
            {
                printf("key must not contain duplicate characters\n");
                return 1;
            }
        }
    }

// convert all characters in key to uppercase
for (int i = 0; i < strlen(key); i++)
{
    if(islower(key[i]))
    {
        key[i] = toupper(key[i]);
    }
}

// prompt the user for plaintext to cipher
string plaintext = get_string("plaintext: ");

// print ciphertext
printf("ciphertext: ");

for (int i = 0; i < strlen(plaintext); i++)
  {
    if (isupper(plaintext[i]))
    {
        int letter = plaintext[i] - 'A';
        printf("%c" , key[letter]);
    }
    else if (islower(plaintext[i]))
    {
        int letter = plaintext[i] - 'a';
        printf("%c" , key[letter] + 'a' - 'A');
    }
    else
    {
         printf("%c" , plaintext[i]);
    }
  }
printf("\n");
return 0;
}
