# pytest -s  --cov=.. --cov-report=html test_networkc.py

import networkx as nx
import numpy as np
import pytest

import networkc as nc

from .util import make_large_graph


@pytest.fixture(scope="function")
def make_learge_dense_random_graph():
    # setup
    G = make_large_graph(num_nodes=1000, edge_density=1)
    # test
    yield G
    # teardown
    pass


@pytest.fixture(scope="function")
def make_small_random_graph():
    # setup
    G = make_large_graph(num_nodes=10, edge_density=0.5)
    # test
    yield G
    # teardown
    pass


@pytest.fixture(scope="function")
def make_sparse_random_graph():
    # setup
    G = make_large_graph(num_nodes=100, edge_density=0.1)
    # test
    yield G
    # teardown
    pass
