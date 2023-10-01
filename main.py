from test.test_util import generate_big_graph, networkc_floyd_warshall

import networkx as nx


def main():
    graph = generate_big_graph(num_nodes=10)
    print(graph)
    res = networkc_floyd_warshall(graph, weight="weight")
    print(res[0][0])
    print(res[0][1])


if __name__ == "__main__":
    main()
