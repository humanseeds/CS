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
         for (int space = 0; space < height - i - 1; space++)
      {
          printf(" ");
      }
        for (int column = 0; column <= row; j++)
    {
        printf("#");
    }
    printf("  ");

    for (int column = 0; j <= i; j++)
    {
        printf("#");
    }
        printf("\n");
    }
}
