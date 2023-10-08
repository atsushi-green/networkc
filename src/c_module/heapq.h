typedef struct {
    double dist;
    int vertex;
} Node;

typedef struct {
    Node* nodes;
    int len;
    int size;
} PriorityQueue;

PriorityQueue* create_queue(int);
void push(PriorityQueue*, int, double);
Node pop(PriorityQueue*);
void free_queue(PriorityQueue*);
