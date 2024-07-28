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
        // int digit uses the modulo to remove the last number from the WorkingCard
        // after the digit is removed / 10 removes the last digit from the card entirely
    int digit = WorkingCard % 10;
    WorkingCard /= 10;
        // modulo 2 determines if a card is even or odd by a result of 0 or 1 ( a remainder).
        // by using the logic of a boolena experation a 0 or 1 signified true or false
    if (Position % 2 == 0)
    {
        checksum +== digit;
    }
}
}

}

