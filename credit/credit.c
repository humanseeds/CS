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
    // Int workingCard is used to keep the original Card-Number intact to veryify card type later

    int Checksum = 0;
    int Position = 0;
    int WorkingCard = Card_Number

// Now we create a loop that does two functions. Run the loop until Card_Number = 0
while (WorkingCard < 0)
{
    int digit = WorkingCard % 10;   // This modulo gets the last digit from WorkingCard
    WorkingCard /= 10;              // divide by 10 Removes the last Digit from WorkingCard
    if (Position)
}

}

