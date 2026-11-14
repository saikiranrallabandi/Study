#include <stdio.h>

int main() {

    // === Level 1: Normal variable ===
    int age = 25;
    printf("age = %d\n", age);                 // 25
    printf("address of age = %p\n\n", &age);   // some memory address

    // === Level 2: Pointer (one star) ===
    // "ptr" holds the ADDRESS of age
    int* ptr = &age;
    printf("ptr points to: %p\n", ptr);        // same address as &age
    printf("value at ptr: %d\n\n", *ptr);      // 25 (dereference = follow the arrow)

    // === Level 3: Pointer to pointer (two stars) ===
    // "pptr" holds the ADDRESS of ptr
    int** pptr = &ptr;
    printf("pptr points to: %p\n", pptr);      // address of ptr
    printf("*pptr (the pointer): %p\n", *pptr); // same as ptr
    printf("**pptr (the value): %d\n\n", **pptr); // 25 (follow two arrows)

    // === WHY IS THIS USEFUL? ===
    // It lets you MODIFY a pointer from inside a function or loop.

    // Example: the llm.c pattern
    // We have 3 variables we want to point to different parts of memory
    float a, b, c;
    float* vars[] = {&a, &b, &c};  // NOT pointer-to-pointer yet, just addresses

    // But in llm.c, we need to SET where pointers point to:
    float* pa = NULL;  // pointer, currently pointing nowhere
    float* pb = NULL;
    float* pc = NULL;

    // Array of pointer-to-pointer: we can CHANGE where pa, pb, pc point
    float** ptrs[] = {&pa, &pb, &pc};

    // Simulating arena allocation: one big block, slice it up
    float memory[12] = {1,2,3,4, 5,6,7,8, 9,10,11,12};

    int sizes[] = {4, 4, 4};  // each "tensor" gets 4 floats

    float* iterator = memory;
    for (int i = 0; i < 3; i++) {
        *(ptrs[i]) = iterator;    // set pa/pb/pc to point here
        iterator += sizes[i];     // move forward
    }

    // Now pa, pb, pc point into the big memory block!
    printf("=== After arena allocation ===\n");
    printf("pa points to: [%.0f, %.0f, %.0f, %.0f]\n", pa[0], pa[1], pa[2], pa[3]);
    printf("pb points to: [%.0f, %.0f, %.0f, %.0f]\n", pb[0], pb[1], pb[2], pb[3]);
    printf("pc points to: [%.0f, %.0f, %.0f, %.0f]\n", pc[0], pc[1], pc[2], pc[3]);

    // Without **, we couldn't change pa/pb/pc from inside the loop!
    // *(ptrs[i]) = iterator  means "change what ptrs[i] points to"
    //   ptrs[0] = &pa, so *(ptrs[0]) = iterator  means  pa = iterator

    return 0;
}
