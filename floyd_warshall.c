#include <Python.h>

void floyd_warshall(int n, double dist[n][n]) {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

static PyObject* py_floyd_warshall(PyObject* self, PyObject* args) {
    PyObject* py_dist;
    if (!PyArg_ParseTuple(args, "O", &py_dist)) {
        return NULL;
    }

    int n = PyList_Size(py_dist);
    double dist[n][n];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = PyFloat_AsDouble(PyList_GetItem(PyList_GetItem(py_dist, i), j));
        }
    }

    floyd_warshall(n, dist);

    PyObject* py_result = PyList_New(n);
    for (int i = 0; i < n; i++) {
        PyObject* row = PyList_New(n);
        for (int j = 0; j < n; j++) {
            PyList_SetItem(row, j, PyFloat_FromDouble(dist[i][j]));
        }
        PyList_SetItem(py_result, i, row);
    }

    return py_result;
}

static PyMethodDef methods[] = {
    {"floyd_warshall", py_floyd_warshall, METH_VARARGS, "Execute Floyd-Warshall Algorithm"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "floyd_warshall_module",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_floyd_warshall_module(void) {
    return PyModule_Create(&module);
}
