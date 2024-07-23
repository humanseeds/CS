#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int row = 0; row < height; row++)
    {
         for (int j = 0; j < n - i - 1; j++)
      {
          printf(" ");
      }
        for (int column = 0; column <= row; j++)
    {
        printf("#");
    }
    printf("  ");

    for (int j = 0; j <= i; j++)
    {
        printf("#");
    }
        printf("\n");
    }
}
