import networkx as nx
from test_util import generate_big_graph, networkc_floyd_warshall

import networkc as nc


def test_flod_warchall():
    graph = generate_big_graph(num_nodes=10)
    res_x = nx.floyd_warshall(graph, weight="weight")
    res_c = nc.floyd_warshall(graph, weight="weight")

    for i in range(len(res_c)):
        for j in range(len(res_c)):
            assert res_x[i][j] == res_c[i][j], f"{res_x[i][j]} != {res_c[i][j]}"
    print("OK")


def test_all_pairs_dijkstra_path():
    graph = generate_big_graph(num_nodes=10)
    res_x = dict(nx.all_pairs_dijkstra_path(graph, weight="weight"))
    res_c = nc.all_pairs_dijkstra_path(graph, weight="weight")
    # key一致の確認
    assert sorted(list(res_x.keys())) == sorted(list(res_c.keys()))

    for k1 in res_x.keys():
        for k2 in res_x[k1].keys():
            assert res_x[k1][k2] == res_c[k1][k2], f"{res_x[k1][k2]} != {res_c[k1][k2]}"


if __name__ == "__main__":
    test_flod_warchall()
    test_all_pairs_dijkstra_path()
