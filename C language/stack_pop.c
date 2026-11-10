#include <stdio.h>
#include <stdlib.h>

typedef struct {
    void **data;
    int count;
    int capacity;
} Stack;

void stack_init(Stack *s, int capacity) {
    s->data = malloc(capacity * sizeof(void *));
    s->count = 0;
    s->capacity = capacity;
}


void push(Stack *s, void *item) {
    s->data[s->count] = item;
    s->count++;
}


void *pop(Stack *s) {
    if (s->count == 0) return NULL;
    s->count--;
    return s->data[s->count];
}



int main(){
    Stack s;

    int a = 10, b = 20, c = 30;

    push(&s, &a);   // stack: [10]
    push(&s, &b);   // stack: [10, 20]
    push(&s, &c);   // stack: [10, 20, 30]

    int *top = (int *)pop(&s);
    printf("%d\n", *top);

    return 0;

}