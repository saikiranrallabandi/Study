#include <stdio.h>

typedef union {
    int age;
    char *name;
} age_or_name_t;

int main() {
    age_or_name_t val;

    val.age = 25;
    printf("Age: %d\n", val.age);

    val.name = "Saikiran";
    printf("Name: %s\n", val.name);
    printf("Age: %d\n", val.age);

    printf("Size: %1lu\n", sizeof(val));

    return 0;
}