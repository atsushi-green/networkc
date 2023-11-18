#include "util.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/*配列の確保*/
/* 3次元配列の領域確保 */
double*** malloc_3dim_array(int n1, int n2, int n3)
{
    int i, j;
    double*** array;
    size_t size_n2 = n2 * sizeof(double*);
    size_t size_n3 = n3 * sizeof(double);

    array = (double***)malloc(n1 * sizeof(double**));
    for (i = 0; i < n1; i++) {
        array[i] = (double**)malloc(size_n2);
        for (j = 0; j < n2; j++)
            array[i][j] = (double*)malloc(size_n3);
    }
    return array;
}

double** malloc_2dim_array(int n1, int n2)
{
    int i;
    double** array;
    size_t size_n2 = n2 * sizeof(double*);
    array = (double**)malloc(n1 * sizeof(double*));
    for (i = 0; i < n1; i++) {
        array[i] = (double*)malloc(size_n2);
    }
    return array;
}

void free_2dim_array(double** array, int n1)
{
    int i;
    for (i = 0; i < n1; i++) {
        free(array[i]);
    }
    free(array);
}
/* 3次元配列の開放 */
void free_3dim_array(double*** array, int n1, int n2)
{
    int i, j;
    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++)
            free(array[i][j]);
        free(array[i]);
    }
    free(array);
}

void print_2dim_array(double** array, int n1, int n2)
{
    int i, j;
    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++) {
            printf("%lf ", array[i][j]);
        }
        printf("\n");
    }
}
