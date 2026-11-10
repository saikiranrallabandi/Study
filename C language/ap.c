#include <stdio.h>

int main(){
    int v1 = 1;
    int v2 = 1;

    int *ptr = &v1;
    printf("%d\n", *ptr);
}