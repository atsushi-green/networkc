#include "heapq.h"
#include <stdlib.h>

PriorityQueue* create_queue(int size)
{
    PriorityQueue* q = malloc(sizeof(PriorityQueue));
    q->nodes = malloc(size * sizeof(Node));
    q->len = 0;
    q->size = size;
    return q;
}

void push(PriorityQueue* q, int vertex, double dist)
{
    int i = q->len++;
    while (i && q->nodes[(i - 1) / 2].dist > dist) {
        q->nodes[i] = q->nodes[(i - 1) / 2];
        i = (i - 1) / 2;
    }
    q->nodes[i].dist = dist;
    q->nodes[i].vertex = vertex;
}

Node pop(PriorityQueue* q)
{
    Node ret = q->nodes[0];
    int i = 0;
    int j;
    Node tmp = q->nodes[--q->len];
    while ((j = 2 * i + 1) < q->len) {
        if (j + 1 < q->len && q->nodes[j].dist > q->nodes[j + 1].dist)
            j++;
        if (q->nodes[j].dist >= tmp.dist)
            break;
        q->nodes[i] = q->nodes[j];
        i = j;
    }
    q->nodes[i] = tmp;
    return ret;
}

void free_queue(PriorityQueue* q)
{
    free(q->nodes);
    free(q);
}
