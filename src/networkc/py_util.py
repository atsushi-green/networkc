from collections import defaultdict
from typing import Any, Dict, List

import networkx as nx
import numpy as np


def list2defaultdict(list_of_list: List[List[float]], node_names: List[Any]) -> Dict[Any, Dict[Any, float]]:
    res = defaultdict(lambda: defaultdict(float))
    for i, node_a in enumerate(node_names):
        for j, node_b in enumerate(node_names):
            res[node_a][node_b] = list_of_list[i][j]
    return dict(res)


def G2edgelist(G: nx.Graph, weight: str = "weight"):
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # infを-1に変換する
    weight_matrix = np.where(weight_matrix == np.inf, -1.0, weight_matrix)
    # weight_matrixの対角成分を0にしてList化する
    np.fill_diagonal(weight_matrix, 0)
    return weight_matrix.tolist()
