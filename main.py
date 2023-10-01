import floyd_warshall_module


def main():
    graph = [
        [0, 3, float("inf"), 7, 5],
        [8, 0, 2, float("inf"), 1],
        [5, float("inf"), 0, 1, 1],
        [2, float("inf"), 3, 0, 1],
        [2, 3, float("inf"), 2, 0],
    ]

    result = floyd_warshall_module.floyd_warshall(graph)
    print(result)

    # [[0.0, 3.0, 5.0, 6.0, 4.0],
    #  [3.0, 0.0, 2.0, 3.0, 1.0],
    #  [3.0, 4.0, 0.0, 1.0, 1.0],
    #  [2.0, 4.0, 3.0, 0.0, 1.0],
    #  [2.0, 3.0, 5.0, 2.0, 0.0]]


if __name__ == "__main__":
    main()
