#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long CreditCard#;
    do
    {
        printf(" Please input Credit Card #: ");
        card = get_long("Card #: ");
    }
    while (card < 0);
