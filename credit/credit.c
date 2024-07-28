// Include libraries to pull functions from

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prompt the user for a Credit Card number. if card number is lesss than 0 user is asked again
    // until one is given.

    long Card_Number = get_long("Please Input Credit Card Number: ");
    while (Card_Number <= 0)
    {
    // this loop continues to politely ask user for a card number and set Long to card number

        printf("Please Try Again \n");
        Card_Number = get_long("Please input Credit Card Number: ");
    }

    // initialize or declare the starting value of the two vaiables evenpositionsum and odd positionsum. Poisition to zero
    // Int workingCard is used to keep the original Card-Number intact to veryify card type later

    int EvenPositionSum = 0;
    int OddPositionSum = 0;
    int Position = 0;
    long WorkingCard = Card_Number;

        // Now we create a loop that does two functions. Run the loop until Card_Number = 0

while (WorkingCard > 0)
{
        // int digit uses the modulo to remove the last number from the WorkingCard
        // after the digit is removed / 10 changes the position by removing the digit

    int digit = WorkingCard % 10;
    WorkingCard /= 10;

        // modulo 2 determines if a number is even or odd by a result of 0 (no remainder) or 1 (a remainder).
        // in Boolean expressions every non zero value is true, zero value is false.
        // If the Modulo of the position is 0, the the position is even (false) and we simply add it to a
        // if the Modulo of a position is 1, the position is odd (true)

    if (Position % 2 == 0)
    {
        EvenPositionSum += digit;  // EvenPositionSum = EvenpositionSum + digit
    }
    else

// The digits at odd positions are doubled, and the sum of the resulting digits are added to OddPositionSum
// if DoubledDigit > 9 we subtract 9 to find the sum in one digit.
// example: doubling 9 results in 18. 1 + 8 = 9 or 18-9
// the ternary operator for the below 'if-else'condition would be
// OddPositionSum += (DoubledDigit > 9) ? (DoubledDigit - 9 ) : DoubledDigit);
    {
        int DoubledDigit = digit * 2;
        if (DoubledDigit > 9 )
        {
            OddPositionSum += (DoubledDigit- 9);
        }
        else
        {
            OddPositionSum += DoubledDigit;
        }
    }
    Position++;
}
int CheckSum = EvenPoitionSum + OddPositionSum;
if (CheckSum % 10 == 0)
{


}
}



