from typing import Any, Dict, List, Optional

import networkc_core as nc_core
import networkx as nx
import numpy as np

from .py_util import list2defaultdict


def floyd_warshall(G: nx.Graph, weight: str = "weight") -> Dict[Any, Dict[Any, float]]:
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Args:
        G (nx.Graph): NetworkX graph.

        weight (str, optional): Edge data key corresponding to the edge weight.
        Defaults to "weight".

    Returns:
        Dict[Any, Dict[Any, float]]: A dictionary, keyed by source and target,
        of shortest paths distances between nodes.
    """
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


def single_source_dijkstra_path(G: nx.Graph, source: Any, weight: str = "weight") -> Dict[Any, List[Any]]:
    """pbd

    Args:
        G (nx.Graph): _description_
        source (Any): _description_
        weight (str, optional): _description_. Defaults to "weight".

    Returns:
        Dict[Any, List[Any]]: _description_
    """
    pass
    # # 隣接(重み)行列を作成する
    # weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # # infを-1に変換する
    # weight_matrix = np.where(weight_matrix == np.inf, -1.0, weight_matrix)
    # # weight_matrixの対角成分を0にしてList化する
    # np.fill_diagonal(weight_matrix, 0)


def all_pairs_dijkstra_path(
    G: nx.Graph, cutoff: Optional[int] = None, weight: Optional[str] = "weight"
) -> Dict[Any, Dict[Any, List[Any]]]:
    """Compute shortest paths between all nodes in a weighted graph.

    Args:
        G (nx.Graph): NetworkX graph

        cutoff (Optional[int], optional): integer or float, optional
        Length (sum of edge weights) at which the search is stopped.
        If cutoff is provided, only return paths with summed weight <= cutoff.
        Defaults to None.

        weight (Optional[str], optional): string or function
        Edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.
        Defaults to "weight".

    Returns:
        Dict[Any, Dict[Any, List[Any]]]: (source, dictionary) Dictionary keyed by target and
        shortest path as the key value.
    """
    # 隣接(重み)行列を作成する
    weight_matrix = nx.to_numpy_array(G, weight=weight, nonedge=np.inf)
    # infを-1に変換する
    weight_matrix = np.where(weight_matrix == np.inf, -1.0, weight_matrix)
    # weight_matrixの対角成分を0にしてList化する
    np.fill_diagonal(weight_matrix, 0)
    if cutoff is None:
        cutoff = -1
    res = nc_core.c_all_pairs_dijkstra_path(weight_matrix.tolist(), cutoff)

    # nodeidを元のnode名に変換しつつ、keyの持たせ方を修正する
    new_res = {}
    index2node = list(G.nodes)
    # 一時的内容が重複した辞書を持つとメモリに厳しいので、popitemで回す
    while res:
        k, path = res.popitem()
        orig, dest = index2node[k[0]], index2node[k[1]]
        if orig not in new_res:
            new_res[orig] = {}
        new_res[orig][dest] = [index2node[v] for v in path]

    return new_res
