import networkx as nx
from test_util import generate_big_graph, networkc_floyd_warshall


def test_flod_warchall():
    graph = generate_big_graph(num_nodes=10)
    res_x = nx.floyd_warshall(graph, weight="weight")

    res_c = networkc_floyd_warshall(graph)

    for i in range(len(res_c)):
        for j in range(len(res_c)):
            assert res_x[i][j] == res_c[i][j], f"{res_x[i][j]} != {res_c[i][j]}"
    print("OK")


if __name__ == "__main__":
    test_flod_warchall()
