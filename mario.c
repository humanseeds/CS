// Library catalog

#include <stdio.h>
#include <cs50.h>

int main(void)
{
   int n;
   do
// prompt height of pyramid with a positive integer
   {
         n = get_int("Height: ");
   }
    while (n < 1);

// print a pyramid based on height N. the rows and columns are equal in size to N. int I represents rows
    for (int i = 0; i < n; i++)
    {
  // Int J determines the columns. Its the same
       for (int j = 0; j < n;  j++)
        {
    // this IF condition controls the spacing and # placement. Ex. Height(N) = 9, and I(row 0) then 9-0+1=8. 8 columns are " " before the "#" is printed. As spaces decrease # increases

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
