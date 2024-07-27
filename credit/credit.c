#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long CreditCardNumber;

    do
    {
        printf(" Please input Credit Card Number: ");
       scanf("%ld/n", & CreditCardNumber);
    }
    while (CreditCardNumber <= 0);

    long workingCC = CreditCardNumber;
