#include <stdio.h>
#include <cs50.h>

int calculate_quarters (int cents)
int calculate_dimes (int cents)
int calculate_nickels (int cents)
int calculate_pennies (int cents)
int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
        while (cents < 0);
        int quaters = calculate_quaters(cents);
        cents = cents - (quaters * 25);
}

int calculate_quarters (int cents)
{
    int quarters = 0;
    while (cents >= 25)
    {
        quaters++;
        cents = cents - 25;
    }
    return quaters;
}
int calculate_dimes (int dimes)
{

}
int calculate_nickels (int nickels)
{

}
int calculate_pennies (int pennies)
{

}

