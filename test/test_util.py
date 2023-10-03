import datetime
import random
from functools import wraps

import networkx as nx

import networkc as nc

random.seed(0)


def generate_big_graph(num_nodes: int = 1000, edge_density: float = 0.5) -> nx.Graph:
    graph = nx.DiGraph()
    graph.add_nodes_from(range(0, num_nodes))
    for i in range(0, num_nodes):
        for j in range(0, num_nodes):
            # edge_densityの確率で辺を追加する
            if random.random() <= edge_density and i != j:
                graph.add_edge(i, j, weight=(random.randint(1, 100000) / 100))
    return graph


def networkc_floyd_warshall(graph: nx.DiGraph, weight: str = "weight") -> list[list[float]]:
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(graph, weight=weight).tolist()
    # print(weight_matrix)
    return nc.floyd_warshall(weight_matrix)


def calc_func_time(f: callable):
    """実行時間を測定するラッパー関数

    Args:
        f (callable): _description_

    Returns:
        _type_: _description_
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = f(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"elapsed time: {f.__name__}: { end - start }")
        return result

    return wrapper
