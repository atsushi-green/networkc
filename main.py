import time
from test.test_util import generate_big_graph

import networkx as nx

import networkc as nc


def main():
    G = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C", "D"])

    G.add_edge("A", "B", weight=1)
    G.add_edge("B", "C", weight=2)
    G.add_edge("C", "D", weight=1)
    G.add_edge("D", "A", weight=1)
    G = generate_big_graph(num_nodes=1000)

    start = time.time()
    res = nc.floyd_warshall(G, weight="weight")
    print("C言語実装のfloyd_warshall", time.time() - start)
    print(res["A"]["D"])

    start = time.time()
    res_orig = nx.floyd_warshall(G, weight="weight")
    print("NetworkX実装のfloyd_warshall", time.time() - start)
    print(res_orig["A"]["D"])
    print(res == res_orig)


if __name__ == "__main__":
    main()
