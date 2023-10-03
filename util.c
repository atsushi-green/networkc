#include "util.h"
#include <stdio.h>
#include <stdlib.h>

/*配列の確保*/
/* 3次元配列の領域確保 */
double*** malloc_3dim_array(int n1, int n2, int n3)
{
    int i, j;
    double*** array;
    array = (int***)malloc(n1 * sizeof(int**));
    for (i = 0; i < n1; i++) {
        array[i] = (double**)malloc(n2 * sizeof(double*));
        for (j = 0; j < n2; j++)
            array[i][j] = (double*)malloc(n3 * sizeof(double));
    }
    return array;
}

double** malloc_2dim_array(int n1, int n2)
{
    int i;
    double** array;
    array = (double**)malloc(n1 * sizeof(double*));
    for (i = 0; i < n1; i++) {
        array[i] = (double*)malloc(n2 * sizeof(double*));
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
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}