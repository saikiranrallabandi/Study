#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *get_full_greeting(char *greeting, char *name, int size){
    char *full_greeting = malloc(size);
    snprintf(full_greeting, size, "%s %s", greeting, name);
    return full_greeting;
}

int main(){
    while (1) {
    char *msg = get_full_greeting("Hello", "Saikiran", 100);
    printf("%s\n", msg);
    // no free(msg) — 100 bytes leaked every iteration
}
    return 0;

}