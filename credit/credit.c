// Include libraries to pull functions from

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt the user for a Credit Card number. if card number is lesss than 0 user is asked again
    // until one is given.

    long Card_Number = get_long("Please Input Credit Card Number: ");
    while (Card_Number <= 0);
    {
    // this loop continues to politely ask user for a card number and set Long to card number
        printf("Please Try Again \n");
        Card_Number = getlong("Please input Credit Card Number: ");
    }
    // initialize Checksum to 0, initialize Digit to 0
    int Checksum = 0;
    int Digit = 0;



}

