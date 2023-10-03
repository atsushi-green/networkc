#include "util.h"
#include <stdio.h>
#include <stdlib.h>

/*配列の確保*/
/* 3次元配列の領域確保 */
int*** malloc_3dim_array(int n1, int n2, int n3)
{
    int i, j;
    int*** array;
    array = (int***)malloc(n1 * sizeof(int**));
    for (i = 0; i < n1; i++) {
        array[i] = (int**)malloc(n2 * sizeof(int*));
        for (j = 0; j < n2; j++)
            array[i][j] = (int*)malloc(n3 * sizeof(int));
    }
    return array;
}

int** malloc_2dim_array(int n1, int n2)
{
    int i;
    int** array;
    array = (int**)malloc(n1 * sizeof(int*));
    for (i = 0; i < n1; i++) {
        array[i] = (int*)malloc(n2 * sizeof(int*));
    }
    return array;
}

void free_2dim_array(int** array, int n1)
{
    int i;
    for (i = 0; i < n1; i++) {
        free(array[i]);
    }
    free(array);
}
/* 3次元配列の開放 */
void free_3dim_array(int*** array, int n1, int n2)
{
    int i, j;
    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++)
            free(array[i][j]);
        free(array[i]);
    }
    free(array);
}

void print_2dim_array(int** array, int n1, int n2)
{
    int i, j;
    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}