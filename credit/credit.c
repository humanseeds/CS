#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long CreditCardNumber = get_long ("Input Credit Card Number: ");
    while (CreditCardNumber <= 0)
        printf("please try again");
}
