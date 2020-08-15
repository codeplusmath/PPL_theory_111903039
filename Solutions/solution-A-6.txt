#include <stdio.h>
int main()
{
    for (int i = 2; i <= 100; i++)
    {
        for (int j = 2; j < i; j++)
        {
            if (i % j == 0)
            {
                break;
            }
            if (i == j)
            {
                printf("%d \n", i);
            }
        }
    }
}
//Output: prime numbers upto 100