//Library catalog
#include <stdio.h>
#include <cs50.h>

int main(void)
{
   int n;
   do
//prompt height of pyramid with a positive integer
   {
         n = get_int("Height: ");
   }
    while (n < 1);

// print a 
    for (int i = 0; i < n; i++)
    {
       for (int j = 0; j < n;  j++)
        {
            if (j < n- i - 1 )
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
                printf("\n");
            }
}
