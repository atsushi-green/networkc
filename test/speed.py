import networkx as nx
from test_util import calc_func_time, generate_big_graph

import networkc as nc

NUM_NODES_LIST = [100, 500, 1000]

EDGE_DENSITY = 0.5


def main():
    for num_nodes in NUM_NODES_LIST:
        print(f"trial: num_nodes: {num_nodes}, edge_density: {EDGE_DENSITY}")
        graph = generate_big_graph(num_nodes=num_nodes, edge_density=EDGE_DENSITY)

        networkx_floyd_warshall(graph)
        networkc_floyd_warshall(graph)

        networkx_all_pairs_dijkstra_path(graph)
        networkc_all_pairs_dijkstra_path(graph)
        print()
        print()


@calc_func_time
def networkx_floyd_warshall(graph):
    return nx.floyd_warshall(graph, weight="weight")


@calc_func_time
def networkc_floyd_warshall(graph):
    # 隣接(重み)行列を作成する
    return nc.floyd_warshall(graph)


@calc_func_time
def networkx_all_pairs_dijkstra_path(graph):
    return nx.all_pairs_dijkstra_path(graph, weight="weight")


@calc_func_time
def networkc_all_pairs_dijkstra_path(graph):
    # 隣接(重み)行列を作成する
    return nc.all_pairs_dijkstra_path(graph)


if __name__ == "__main__":
    main()
