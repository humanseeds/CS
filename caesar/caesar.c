#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// declare a function that will be used
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // make sure the amount of comman line arguments is 2 ( file name and a key number)
    // exit code with an error is not
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // iterate over each character in the key to make sure its a digit
    // Exit with an error code if not
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // convert the key from a string into an integer
    int k = atoi(argv[1]);

    // Promt the user for a plaintext to be deciphered
    string plaintext = get_string("plaintext: ");

    printf("Ciphertext: ");

    // Use the Caesar Cipher to encrypt the plaintext
    for (int j = 0; j < strlen(plaintext); j++)
    {
        char c = plaintext[j];
        printf("%c", rotate(c, k));
    }

    printf("\n");
    return 0;
}

// define a function to rotate the char to int
char rotate(char c, int k)
{
    if (isupper(c))
    {
        return (c - 'A' + k) % 26 + 'A';
    }
    else if (islower(c))
    {
        return (c - 'a' + k) % 26 + 'a';
    }
    else
    {
        return c;
    }
}
