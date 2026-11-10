#include <stdio.h>

typedef enum {
    TYPE_INT,
    TYPE_STRING
} ObjectType;

typedef struct {
    ObjectType type;
    union {
        int int_val;
        char *str_val;
    } data;
} SnekObject;

int main() {
    //create an interger object

    SnekObject obj1;
    obj1.type = TYPE_INT;
    obj1.data.int_val = 42;


    //create a string object;
    SnekObject obj2;
    obj2.type = TYPE_STRING;
    obj2.data.str_val = "Hello";

    // use the tag to know whats inside

    SnekObject objects[2] = {obj1, obj2};

    for (int i = 0; i < 2; i++) {
        switch (objects[i].type) {
            case TYPE_INT:
                printf("INT: %d\n", objects[i].data.int_val);
                break;
            case TYPE_STRING:
                printf("Sre: %s\n", objects[i].data.str_val);
                break;
        }
    }

    return 0;
}