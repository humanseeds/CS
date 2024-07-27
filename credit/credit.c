#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long CreditCardNumber = get_long ("Please Input Credit Card Number: ");

   while (CreditCardNumber <= 0)
   {
    printf("Please Try Again /n");
   }
}
