#include <stdio.h>
void function(int a, int b, int c)
{
    char buffer1[5];
    char buffer2[10];
    int *ret;
    ret = buffer1 + 21;
    (*ret) += 7;
}
int main()
{
    int x;
    x = 0;
    function(1, 2, 3);
    x = 1;
    printf("%d\n", x);
    return 0;
}
// 0x55b8dd659698