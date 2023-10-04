# 実行速度を計測するためのスクリプト
# NUM_NODES_LIST に指定したノード数のグラフを作成し、
# networkx と networkc の メソッド を実行する
import networkx as nx
from util import calc_func_time, make_large_graph

import networkc as nc

NUM_NODES_LIST = [100, 500, 1000]

EDGE_DENSITY = 0.5


def main():
    for num_nodes in NUM_NODES_LIST:
        print(f"trial: num_nodes: {num_nodes}, edge_density: {EDGE_DENSITY}")
        graph = make_large_graph(num_nodes=num_nodes, edge_density=EDGE_DENSITY)

        networkx_floyd_warshall(graph)
        networkc_floyd_warshall(graph)
        print()
        print()


@calc_func_time
def networkx_floyd_warshall(graph):
    return nx.floyd_warshall(graph, weight="weight")


@calc_func_time
def networkc_floyd_warshall(graph):
    # 隣接(重み)行列を作成する
    return nc.floyd_warshall(graph)


if __name__ == "__main__":
    main()
