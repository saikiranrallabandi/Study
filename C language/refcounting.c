#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int value;
    int ref_count;   // how many pointers point to me?
} Object;

Object *create(int val) {
    Object *obj = malloc(sizeof(Object));
    obj->value = val;
    obj->ref_count = 1;   // creator holds one reference
    return obj;
}

void retain(Object *obj) {
    obj->ref_count++;     // someone new points to me
}

void release(Object *obj) {
    obj->ref_count--;     // someone stopped pointing to me
    if (obj->ref_count == 0) {
        printf("Freeing object with value %d\n", obj->value);
        free(obj);        // nobody points to me, goodbye
    }
}

int main() {
    Object *a = create(42);      // ref_count = 1
    retain(a);                    // ref_count = 2 (two pointers to it)
    release(a);                   // ref_count = 1 (still alive)
    release(a);                   // ref_count = 0 → freed

    return 0;
}