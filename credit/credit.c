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
    // initialize or declare the starting value of the two vaiables Checksum and Poisition to zero
    int Checksum = 0;
    int Position = 0;

// Now we create a loop that does two functions. Run the loop until Card_Number = 0
while (Card_Number < 0)
{
    int digit = Card_Number % 10;   //This modulo
    Card_Number /= 10;
}

}

