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
    # TODO: 隣接距離行列の定義を揃える（-1がつながっていないことを表すようにする）
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # weight_matrixの対角成分を0にしてList化する
    np.fill_diagonal(weight_matrix, 0)
    res = nc_core.c_floyd_warshall(weight_matrix.tolist())
    # TODO: ここの変換はできるだけC言語でやる(やれる)
    # defaultdictに変換する
    res = list2defaultdict(res, G.nodes)
    return res


def single_source_dijkstra_path(G: nx.Graph, source: Any, weight: str = "weight") -> dict[Any, List[Any]]:
    pass
    # # 隣接(重み)行列を作成する
    # weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # # infを-1に変換する
    # weight_matrix = np.where(weight_matrix == np.inf, -1.0, weight_matrix)
    # # weight_matrixの対角成分を0にしてList化する
    # np.fill_diagonal(weight_matrix, 0)


def all_pairs_dijkstra_path(G: nx.Graph, weight: str = "weight") -> dict[Any, dict[Any, List[Any]]]:
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # infを-1に変換する
    weight_matrix = np.where(weight_matrix == np.inf, -1.0, weight_matrix)
    print(weight_matrix)
    # 整数化
    weight_matrix = np.array(weight_matrix, dtype=int)
    # weight_matrixの対角成分を0にしてList化する
    np.fill_diagonal(weight_matrix, 0)
    res = nc_core.c_all_pairs_dijkstra_path(weight_matrix.tolist())

    # nodeidを元のnode名に変換しつつ、keyの持たせ方を修正する
    # TODO: ここの変換はできるだけC言語でやる(やれる)
    new_res = {}
    index2node = list(G.nodes)
    for k, path in res.items():
        orig, dest = index2node[k[0]], index2node[k[1]]
        if orig not in new_res:
            new_res[orig] = {}
        new_res[orig][dest] = [index2node[v] for v in path]
        # del res[k]
    return new_res


def G2edgelist(G: nx.Graph, weight: str = "weight"):
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # infを-1に変換する
    weight_matrix = np.where(weight_matrix == np.inf, -1.0, weight_matrix)
    # weight_matrixの対角成分を0にしてList化する
    np.fill_diagonal(weight_matrix, 0)
    return weight_matrix.tolist()