#include <stdio.h>
#include <stdlib.h>

// ============================================================
// GOAL: Understand these two lines from train_gpt2.c:
//
// model->params_memory = malloc_and_point_parameters(&model->params, model->param_sizes);
// freadCheck(model->params_memory, sizeof(float), num_parameters, model_file);
//
// We'll build up step by step.
// ============================================================

// A simple struct (like ParameterTensors but tiny)
typedef struct{
    float* weights;
    float* biases;
} MyParams;

// A simple model (like GPT2 struct but tiny)

typedef struct {
    MyParams params;
    float* params_memory;
    int num_params;
} MyModel;

// ============================================================
// Step 1: Write a binary file (like train_gpt2.py does)
// ============================================================
void create_model_file(const char* filename) {
    float data[8] = {1.1, 2.2, 3.3, 4.4,    // "weights" (4 floats)
                     5.5, 6.6, 7.7, 8.8};    // "biases"  (4 floats)
    FILE* f = fopen(filename, "wb");
    fwrite(data, sizeof(float), 8, f);
    fclose(f);
    printf("Wrote 8 floats to %s\n\n", filename);
}
// ============================================================
// Step 2: malloc_and_point (same pattern as train_gpt2.c)
// ============================================================
float* malloc_and_point(MyParams* params, int weight_size, int bias_size) {
    // Allocate ONE big block for everything
    int total = weight_size + bias_size;
    float* memory = (float*)malloc(total * sizeof(float));




    // Point weights to the START of the block
    params->weights = memory;

    // Point biases to AFTER the weights
    params->biases = memory + weight_size;

    return memory;
}


int main(){
    printf("=== Part A: Binary File I/O ===\n");
    // Write a model file
    create_model_file("tiny_model.bin");

    // Read it back — this is what freadCheck does
    FILE* f = fopen("tiny_model.bin", "rb");  // rb = read binary
    float buffer[8];
    fread(buffer, sizeof(float), 8, f);       // read 8 floats
    fclose(f);

    printf("Read back from file:\n");
    for (int i = 0; i < 8; i++) {
        printf("  buffer[%d] = %.1f\n", i, buffer[i]);
    }

    // ============================================================
    // Part B: Understanding malloc_and_point
    // ============================================================
    printf("\n=== Part B: malloc_and_point ===\n");


    MyModel model;
    int weight_size = 4;
    int bias_size = 4;
    model.num_params = weight_size + bias_size;


    // This is the FIRST line from train_gpt2.c:
    // model->params_memory = malloc_and_point_parameters(...)

    model.params_memory = malloc_and_point(&model.params, weight_size, bias_size);

    printf("After malloc_and_point:\n");
    printf("  params_memory points to: %p\n", model.params_memory);
    printf("  weights points to:       %p (same as params_memory)\n", model.params.weights);
    printf("  biases points to:        %p (params_memory + 4)\n", model.params.biases);

    // ============================================================
    // Part C: Combining both — malloc then fread into it
    // ============================================================
    printf("\n=== Part C: The full pattern ===\n");

    // Open the file
    FILE* model_file = fopen("tiny_model.bin", "rb");

    // This is the SECOND line from train_gpt2.c:
    // freadCheck(model->params_memory, sizeof(float), num_parameters, model_file)
    fread(model.params_memory, sizeof(float), model.num_params, model_file);
    fclose(model_file);

    // Now weights and biases are filled with data from the file!
    printf("After fread into params_memory:\n");
    printf("  weights: [%.1f, %.1f, %.1f, %.1f]\n",
           model.params.weights[0], model.params.weights[1],
           model.params.weights[2], model.params.weights[3]);
    printf("  biases:  [%.1f, %.1f, %.1f, %.1f]\n",
           model.params.biases[0], model.params.biases[1],
           model.params.biases[2], model.params.biases[3]);

    // ============================================================
    // Part D: WHY this works
    // ============================================================
    printf("\n=== Part D: Memory layout ===\n");
    printf("One big block in memory:\n");
    printf("  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n");
    printf("  │ 1.1 │ 2.2 │ 3.3 │ 4.4 │ 5.5 │ 6.6 │ 7.7 │ 8.8 │\n");
    printf("  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n");
    printf("  ↑ weights                ↑ biases\n");
    printf("  ↑ params_memory\n");
    printf("\n");
    printf("fread fills the ENTIRE block from the file.\n");
    printf("weights and biases point INTO the same block.\n");
    printf("No copying needed — they share the memory!\n");

    // Cleanup
    free(model.params_memory);

    return 0;
}
