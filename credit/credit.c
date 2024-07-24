#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card;
    do
    {
        card = get_long("Card #: ");
    }
    while (card < 0);
