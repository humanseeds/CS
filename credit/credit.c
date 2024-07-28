#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long Card_Number = get_long("Please Input Credit Card Number: ");
    while (Card_Number <= 0);
    {
        printf("Please Try Again \n");
        Card_Number = getlong("Please input Credit Card Number: ");
    }
    int checksum = 0
    int Digit = 0
    


}

