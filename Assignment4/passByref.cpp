#include <iostream>
using namespace std;
void swap(int &x, int &y)
{
    int z = x;
    x = y;
    y = z;
}

int main()
{
    int a = 5, b = 7;
    swap(a, b);
    return 0;
}
