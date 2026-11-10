#include "munit.h"
#include "coordinate.h"

munit_case(RUN, test_update_x_does_not_change_original, {
    coordinate_t coord;
    coord.x = 1;
    coord.y = 2;
    coord.z = 3;
    coordinate_update_x(coord, 4);
    munit_assert_int(coord.x, 1);
    munit_assert_int(coord.y, 2);
    munit_assert_int(coord.z, 3);
});

munit_case(RUN, test_update_and_return_x, {
    coordinate_t coord;
    coord.x = 1;
    coord.y = 2;
    coord.z = 3;
    coordinate_t updated = coordinate_update_and_return_x(coord, 4);
    munit_assert_int(updated.x, 4);
    munit_assert_int(updated.y, 2);
    munit_assert_int(updated.z, 3);
});

munit_case(SUBMIT, test_original_unchanged_after_return, {
    coordinate_t coord;
    coord.x = 10;
    coord.y = 20;
    coord.z = 30;
    coordinate_t updated = coordinate_update_and_return_x(coord, 99);
    munit_assert_int(coord.x, 10);
    munit_assert_int(updated.x, 99);
});

int main(int argc, char **argv)
{
    int submit = (argc > 1 && strcmp(argv[1], "submit") == 0);

    test_update_x_does_not_change_original();
    test_update_and_return_x();

    if (submit) {
        test_original_unchanged_after_return();
    } else {
        printf("Skipping SUBMIT tests (run with: ./coordinate_tests submit)\n");
    }

    printf("All tests passed\n");
    return 0;
}
