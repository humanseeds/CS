//Library catalog
#include <stdio.h>
#include <cs50.h>

int main(void)
{
   int n;
   do
   {
         n = get_int("Height: ");
    }
    while (n < 1);

    {
        n = get_int("Height: ");
    }
    printf("%i#\n", n + 1);
}
