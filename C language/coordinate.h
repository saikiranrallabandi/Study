#ifndef COORDINATE_H
#define COORDINATE_H

typedef struct {
    int x;
    int y;
    int z;
} coordinate_t;

void coordinate_update_x(coordinate_t coord, int new_x);
coordinate_t coordinate_update_and_return_x(coordinate_t coord, int new_x);

#endif
