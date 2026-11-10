#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

float add(int a, int b)
{
   return (float)(a + b);
}

int max(int max_threads, int memory_per_thread){
   return max_threads * memory_per_thread;
}

void init(int max_threads, int memory_per_thread){
   printf("Initializing with %d threads and %d memory per thread\n", max_threads, memory_per_thread);
   int max_memory = max(max_threads, memory_per_thread);
   printf("Max memory: %d\n", max_memory);

}


int main()
{
   printf("hello world\n");

   char *name = "John";
   printf("Hello, %s\n", name);

   int age = 20;
   float height = 1.75;
   char *height_str = "1.75";

   printf("Name: %s\n", name);
   printf("Age: %d\n", age);
   printf("Height: %f\n", height);
   printf("Height: %s\n", height_str);

   float result = add(1, 2);
   printf("Result: %f\n", result);

   printf("size of bool: %zu\n", sizeof(bool));
   printf("size of int: %zu\n", sizeof(int));
   printf("size of float: %zu\n", sizeof(float));
   printf("size of double: %zu\n", sizeof(double));
   printf("size of char: %zu\n", sizeof(char));
   printf("size of short: %zu\n", sizeof(short));
   printf("size of long: %zu\n", sizeof(long));
   printf("size of long long: %zu\n", sizeof(long long));

   init(10, 100);

   return 0;
}
