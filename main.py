import networkx as nx

import networkc as nc


def main():
    G = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C", "D"])

    G.add_edge("A", "B", weight=1)
    G.add_edge("B", "C", weight=2)
    G.add_edge("C", "D", weight=1)
    G.add_edge("D", "A", weight=1)

    res = nc.floyd_warshall(G, weight="weight")
    print(res["A"]["D"])

    res_orig = nx.floyd_warshall(G, weight="weight")
    print(res_orig["A"]["D"])

    print(res == res_orig)
    nx.all_pairs_dijkstra_path


if __name__ == "__main__":
    main()
