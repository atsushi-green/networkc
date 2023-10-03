/*
build: $ python setup.py build_ext --inplace
pip: $ pip install ./networkc
*/

#include <Python.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#define INF INT_MAX

/*floyd_warshall*/
void c_floyd_warshall(int n, double dist[n][n])
{
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

/*dijkstra*/
void dijkstra(int n, int graph[][n], int path[][n][n])
{
    int dist[n], prev[n], visited[n];
    // 初期化
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                path[i][j][k] = -1;
            }
        }
    }
    // 各sourceノードに対して、dijkstraを実行
    for (int source = 0; source < n; source++) {
        printf("source: %d\n", source);
        // 初期化
        for (int i = 0; i < n; i++) {
            dist[i] = INF;
            prev[i] = -1;
            visited[i] = 0;
        }
        dist[source] = 0; // ソースノードからソースノードへの距離は0

        for (int count = 0; count < n; count++) {
            int u = -1; // 未訪問で最も距離が小さいノード
            int min_distance = INF;
            // 未訪問で最も距離が小さいノードを見つける
            // TODO: Priority Queue を使うと高速化できる
            for (int i = 0; i < n; i++) {
                if (!visited[i] && (dist[i] < min_distance)) {
                    min_distance = dist[i];
                    u = i;
                }
            }
            if (u == -1) {
                continue;
            }
            // printf("uが決定: %d\n", u);
            // fflush(stdout);
            // ノードuを訪問済みにする
            visited[u] = 1;

            // uと隣接するノードの距離を更新する
            for (int v = 0; v < n; v++) {
                if (!visited[v] && graph[u][v] != INF && dist[u] != INF && dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                    prev[v] = u;
                    printf("uと隣接するノードの距離を更新: dist[%d] = %d\n", v, dist[v]);
                }
            }
        }
        // for (int i = 0; i < n; i++) {
        //     printf("%d ", dist[i]);
        // }

        // for (int i = 0; i < n; i++) {
        //     printf("%d ", prev[i]);
        // }
        // printf("\n");
        // target への最短経路をpathに格納
        for (int target = 0; target < n; target++) {
            if (dist[target] == INF) {
                // 辿り着けない時は、-1を入れて終わり
                path[source][target][0] = -1;
                continue;
            }
            if (source != target && dist[target] != INF) {
                int index = 0;
                int t = target;
                int tempPath[n]; // 逆順のpathを一時的に入れておく配列

                while (t != source) {
                    tempPath[index] = t;
                    t = prev[t];
                    index++;
                }
                // tempPath[index] = source;
                // tempPathを逆順にしてpathに入れる
                for (int i = 0; i < index + 1; i++) {
                    path[source][target][i] = tempPath[index - i - 1];
                }

            } else if (source == target) {
                path[source][target][0] = source;
            }
        }
    }
    // ソース0からターゲット3への最短経路を表示
    // printf("source: %d, target: %d\n", 0, 3);
    // printf("aaaaa %d aaaaa\n", path[0][3][0]);
    // for (int i = 0; i < n; i++) {
    //     printf("%d \n", path[0][3][i]);
    // }
    printf("bbbbbbb");

    fflush(stdout);
}

static PyObject* py_all_pairs_dijkstra_path(PyObject* self, PyObject* args)
{
    printf("C py_all_pairs_dijkstra_path 実行開始: \n");
    PyListObject* inputList;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &inputList)) {
        return NULL;
    }
    // TODO: mallocで動的に確保する(サイズが大きいと segmentation fault になる)
    int n = PyList_Size(inputList);
    // int*** path = malloc_3dim_array(n, n, n);
    // int** graph = malloc_2dim_array(n, n);
    int graph[n][n];
    int path[n][n][n];
    // graph に隣接重み行列を入れる
    // path には、経路の最初のノード（自分自身のノードiを入れる）
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            path[i][j][0] = i;
            path[i][j][1] = -1;
            PyObject* pyVal = PyList_GetItem(PyList_GetItem(inputList, i), j);
            if (PyLong_AsLong(pyVal) == -1) {
                graph[i][j] = INF;
            } else {
                graph[i][j] = (int)PyLong_AsLong(pyVal);
            }
        }
    }
    printf("C　dijkstra実行開始: \n");
    fflush(stdout);
    // 最短経路を計算
    dijkstra(n, graph, path);
    PyObject* result = PyDict_New();
    // iからjへの経路をresultに入れる
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            PyObject* pathList = PyList_New(0);
            int k = 0, u = i;
            int prev = -1;
            if (path[i][j][0] == -1) {
                // 経路がない場合は、Pythonの辞書に追加しない-1を入れて終わり
                continue;
            }
            while (u != j) {
                // if (u != prev) {
                //     // 同じノードを連続で辿っているものは飛ばす
                //     PyList_Append(pathList, PyLong_FromLong(u));
                // }
                PyList_Append(pathList, PyLong_FromLong(u));
                prev = u;
                u = path[i][j][k++];
            }
            PyList_Append(pathList, PyLong_FromLong(j)); // 最後にjを追加して経路が完成
            PyObject* key = PyTuple_Pack(2, PyLong_FromLong(i), PyLong_FromLong(j));
            PyDict_SetItem(result, key, pathList);
            Py_DECREF(key);
            Py_DECREF(pathList);
        }
    }
    // TODO: ここでmallocしたメモリ解放
    // free_3dim_array(path, n, n, n);
    return result;
}

static PyObject* py_floyd_warshall(PyObject* self, PyObject* args)
{
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

    c_floyd_warshall(n, dist);

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

/*メソッドの定義 (ここに登録するメソッドを書き並べる)*/
static PyMethodDef methods[] = {
    { "c_floyd_warshall", py_floyd_warshall, METH_VARARGS, "Execute Floyd-Warshall Algorithm" },
    { "c_all_pairs_dijkstra_path", py_all_pairs_dijkstra_path, METH_VARARGS, "Execute Floyd Warshall Algorithm for path" },
    // TODO: ここに足していけばOK
    { NULL, NULL, 0, NULL } // 終了を示す番兵なので消してはいけない
};

// モジュールの定義
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "networkc_core", // module name
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_networkc_core(void)
{
    return PyModule_Create(&module);
}
