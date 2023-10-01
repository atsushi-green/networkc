from collections import defaultdict
from typing import Any, Dict, List

import networkc_core as nc_core
import networkx as nx
import numpy as np


def list2defaultdict(list_of_list: List[List[float]], node_names: List[Any]) -> Dict[Any, defaultdict[Any, float]]:
    res = defaultdict(lambda: defaultdict(float))
    for i, node_a in enumerate(node_names):
        for j, node_b in enumerate(node_names):
            res[node_a][node_b] = list_of_list[i][j]
    return dict(res)


def floyd_warshall(G: nx.Graph, weight: str = "weight") -> dict[Any, defaultdict[Any, float]]:
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # weight_matrixの対角成分を0にしてList化する
    np.fill_diagonal(weight_matrix, 0)
    res = nc_core.c_floyd_warshall(weight_matrix.tolist())
    # defaultdictに変換する
    res = list2defaultdict(res, G.nodes)
    return res
