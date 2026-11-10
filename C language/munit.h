#ifndef MUNIT_H
#define MUNIT_H

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {
    RUN,
    SUBMIT
} munit_mode;

#define munit_case(MODE, NAME, BODY) \
    static void NAME(void)           \
    {                                \
        printf("Running %s\n", #NAME); \
        BODY                         \
        printf("  OK\n");            \
    }

#define munit_assert_double_equal(actual, expected)                         \
    do {                                                                    \
        double _actual = (double)(actual);                                  \
        double _expected = (double)(expected);                              \
        if (fabs(_actual - _expected) > 0.0001) {                           \
            printf("  FAIL: %s == %s (%f != %f)\n",                         \
                   #actual, #expected, _actual, _expected);                 \
            exit(1);                                                        \
        }                                                                   \
    } while (0)

#define munit_assert_int(actual, expected)                                  \
    do {                                                                    \
        int _actual = (actual);                                             \
        int _expected = (expected);                                         \
        if (_actual != _expected) {                                         \
            printf("  FAIL: %s == %s (%d != %d)\n",                         \
                   #actual, #expected, _actual, _expected);                 \
            exit(1);                                                        \
        }                                                                   \
    } while (0)

#define munit_assert_string_equal(actual, expected)                         \
    do {                                                                    \
        const char *_actual = (actual);                                     \
        const char *_expected = (expected);                                 \
        if (strcmp(_actual, _expected) != 0) {                              \
            printf("  FAIL: %s == %s (\"%s\" != \"%s\")\n",                 \
                   #actual, #expected, _actual, _expected);                 \
            exit(1);                                                        \
        }                                                                   \
    } while (0)

#endif

