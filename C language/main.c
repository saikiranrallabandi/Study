#include "munit.h"
#include "exercise.h"

munit_case(RUN, test_too_cold, {
    char *result = get_temperature_status(69);
    munit_assert_string_equal(result, "too cold");
});

munit_case(RUN, test_too_hot, {
    char *result = get_temperature_status(91);
    munit_assert_string_equal(result, "too hot");
});

munit_case(RUN, test_just_right, {
    char *result = get_temperature_status(80);
    munit_assert_string_equal(result, "just right");
});

munit_case(SUBMIT, test_boundaries, {
    munit_assert_string_equal(get_temperature_status(70), "just right");
    munit_assert_string_equal(get_temperature_status(90), "just right");
});

int main(int argc, char **argv)
{
    int submit = (argc > 1 && strcmp(argv[1], "submit") == 0);

    test_too_cold();
    test_too_hot();
    test_just_right();

    if (submit) {
        test_boundaries();
    } else {
        printf("Skipping SUBMIT tests (run with: ./average_tests submit)\n");
    }

    printf("All tests passed\n");
    return 0;
}
