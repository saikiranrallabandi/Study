#include <stdio.h>
#include <string.h>

typedef struct {
    char buffer[64];
    int length;

} TextBuffer;

int main() {

    char *msg = "Hello";

    printf("strlen: %zu\n", strlen(msg));

    int i = 0;

    while (msg[i] != '\0') {
        printf("msg[%d] = '%c'\n", i, msg[i]);
        i++;
    }
    printf("msg[%d] = '\\0'\n", i);



    TextBuffer tb;

    strcpy(tb.buffer, "Hello");
    tb.length = 5;
    printf("Direct: %s (len %d)\n", tb.buffer, tb.length);

    TextBuffer *ptr = &tb;
    strcat(ptr->buffer, "world");
    ptr->length = strlen(ptr->buffer);
    printf("Pointer: %s (len %d)\n", ptr->buffer, ptr->length);
    return 0;
}