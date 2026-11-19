#include <stdio.h>
#include <stdlib.h>

// === Simple mallocCheck (same idea as llm.c) ===
void* mallocCheck(size_t size) {
    void* ptr = malloc(size);
    if (ptr == NULL) {
        printf("malloc failed! Requested %zu bytes\n", size);
        exit(1);
    }
    return ptr;
}

// === A simple struct (like a mini DataLoader) ===
typedef struct {
    int B;          // batch size
    int T;          // sequence length
    int* inputs;    // pointer — will be allocated with mallocCheck
    int* targets;   // pointer — will be allocated with mallocCheck
} MiniLoader;

// === Fill the loader with fake data ===
void loader_init(MiniLoader* loader, int B, int T) {
    loader->B = B;
    loader->T = T;

    // This is the pattern from dataloader.h:
    // loader->inputs = (int*)mallocCheck(B * T * sizeof(int));
    loader->inputs  = (int*)mallocCheck(B * T * sizeof(int));
    loader->targets = (int*)mallocCheck(B * T * sizeof(int));

    // Fill with fake data: inputs = [0,1,2,...], targets = [1,2,3,...]
    for (int i = 0; i < B * T; i++) {
        loader->inputs[i]  = i;
        loader->targets[i] = i + 1;
    }
}

// === Print the data ===
void loader_print(MiniLoader* loader) {
    int B = loader->B;
    int T = loader->T;

    printf("B=%d, T=%d, total tokens=%d\n\n", B, T, B * T);

    for (int b = 0; b < B; b++) {
        printf("Batch %d:\n", b);
        printf("  inputs:  [");
        for (int t = 0; t < T; t++) {
            printf("%d", loader->inputs[b * T + t]);
            if (t < T - 1) printf(", ");
        }
        printf("]\n");

        printf("  targets: [");
        for (int t = 0; t < T; t++) {
            printf("%d", loader->targets[b * T + t]);
            if (t < T - 1) printf(", ");
        }
        printf("]\n\n");
    }
}

// === Free everything ===
void loader_free(MiniLoader* loader) {
    free(loader->inputs);
    free(loader->targets);
    printf("Freed inputs and targets\n");
}

int main() {
    int B = 2;  // 2 batches
    int T = 4;  // 4 tokens each

    // Create struct on stack, pass pointer to init
    MiniLoader loader;
    loader_init(&loader, B, T);

    // Print what we got
    loader_print(&loader);

    // Clean up
    loader_free(&loader);

    return 0;
}
