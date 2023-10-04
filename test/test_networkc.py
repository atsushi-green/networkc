# Test networkc
# pytest -s  --cov=.. --cov-report=html test_networkc.py
from typing import Callable, TypeVar

import networkx as nx
import pytest

FixtureFunction = TypeVar("FixtureFunction", bound=Callable[..., object])
import networkc as nc


class TestNetworkc:
    @pytest.mark.smoke
    def test_flod_warchall(self, make_small_random_graph: FixtureFunction):
        G = make_small_random_graph
        # setup
        res_x = dict(nx.floyd_warshall(G, weight="weight"))
        res_c = nc.floyd_warshall(G, weight="weight")
        # eval
        assert res_x == res_c
        # teardown
        pass

    def test_flod_warchall2(self, make_learge_dense_random_graph: FixtureFunction):
        # 巨大グラフに対するテスト
        G = make_learge_dense_random_graph
        # setup
        res_x = dict(nx.floyd_warshall(G, weight="weight"))
        res_c = nc.floyd_warshall(G, weight="weight")
        # eval
        assert res_x == res_c
        # teardown
        pass

    @pytest.mark.smoke
    def test_all_pairs_dijkstra_path(self, make_small_random_graph: FixtureFunction):
        G = make_small_random_graph
        # setup
        res_x = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))
        res_c = nc.all_pairs_dijkstra_path(G, weight="weight")
        # eval
        assert res_x == res_c
        # teardown
        pass

    @pytest.mark.smoke
    def test_all_pairs_dijkstra_path2(self, make_learge_dense_random_graph: FixtureFunction):
        # 巨大グラフに対するテスト
        G = make_learge_dense_random_graph
        # setup
        res_x = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))
        res_c = nc.all_pairs_dijkstra_path(G, weight="weight")
        # eval
        assert res_x == res_c
        # teardown
        pass
