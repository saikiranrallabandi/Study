#include <stdio.h>

// define the struct
typedef struct {
    int age;
    char grade;
} Student;

int main() {
    // create a student struct
    Student s;
    s.age = 25;
    s.grade = 'A';

    printf("Student age: %d\n", s.age);
    printf("Student grade: %c\n", s.grade);

    // or initialize a struct with a struct initializer
    Student s2 = {25, 'A'};
    printf("Student age: %d\n", s2.age);
    printf("Student grade: %c\n", s2.grade);

}