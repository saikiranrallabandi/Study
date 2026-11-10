#include <stdio.h>

int main() {
    int x = 42;
    int *p = &x;

    printf("Value of x: %d\n", x);
    printf("Address of x:    %p\n", &x);
    printf("Value of p:      %p\n", p);
    printf("What p points to: %d\n", *p);
    printf("Size of p:       %lu\n", sizeof(p));
    printf("Size of x:       %lu\n", sizeof(x));

    return 0;
}