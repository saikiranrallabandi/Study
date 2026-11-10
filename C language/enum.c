#include <stdio.h>

typedef enum {
    RED,
    GREEN,
    BLUE
} color;

int main() {
    color myColor = GREEN;

    if (myColor == GREEN) {
        printf("Go!\n");
    }

    printf("GREEN = %d\n", myColor);

    return 0;
}