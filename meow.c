#include <stdio.h>

void meow(void)
{
    printf("meow\n");
}

int main(void)
{
   int i = 3;
   while (i > 0)
   {
        meow();
   }
}

