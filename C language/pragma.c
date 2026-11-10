#include <stdio.h>
#include <omp.h>
#include <time.h>

// A function that does some heavy work (sum a big array)
void heavy_work(float* result, float* a, float* b, int N) {
    for (int i = 0; i < N; i++) {
        result[i] = a[i] * b[i] + a[i] - b[i];  // some math to keep CPU busy
    }
}

int main() {
    int N = 100000000;  // 100 million elements
    static float a[100000000];
    static float b[100000000];
    static float c[100000000];

    // fill arrays
    for (int i = 0; i < N; i++) {
        a[i] = (float)i * 0.001f;
        b[i] = (float)i * 0.002f;
    }

    // ========== WITHOUT OpenMP ==========
    clock_t start1 = clock();

    for (int i = 0; i < N; i++) {
        c[i] = a[i] * b[i] + a[i] - b[i];
    }

    clock_t end1 = clock();
    double time1 = (double)(end1 - start1) / CLOCKS_PER_SEC;
    printf("Without OpenMP (1 core):  %.4f seconds\n", time1);

    // ========== WITH OpenMP ==========
    double start2 = omp_get_wtime();  // omp has its own timer (wall clock)

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        c[i] = a[i] * b[i] + a[i] - b[i];
    }

    double end2 = omp_get_wtime();
    double time2 = end2 - start2;
    printf("With OpenMP (%d cores):   %.4f seconds\n", omp_get_max_threads(), time2);

    printf("Speedup: %.1fx faster\n", time1 / time2);

    return 0;
}
