#include <stdio.h>

typedef enum {
    HTTP_OK,
    HTTP_NOT_FOUND,
    HTTP_INTERNAL_ERROR,
} HttpErrorCode;

char *http_to_start(HttpErrorCode code);

char *http_to_start(HttpErrorCode code) {
    switch (code) {
        case HTTP_OK:
           return "200 ok";
        case HTTP_NOT_FOUND:
           return "404 Not Found";
        case HTTP_INTERNAL_ERROR:
           return "500 Internal Server Error";
        default:
           return "Unknown";
    }
}


int main(){

    HttpErrorCode err = HTTP_NOT_FOUND;

    printf("%s\n", http_to_start(err));

    printf("%s\n", http_to_start(HTTP_OK));

    return 0;

}