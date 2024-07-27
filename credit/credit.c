#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long CreditCardNumber;
    do
    {
        CreditCardNumber = get_long("Input Credit Card Number: ");
        if (CreditCardNumber <= 0)
        {
            printf("Please Try Again \n");
        }
        while (CreditCardNumber <= 0 );
        }
    }



