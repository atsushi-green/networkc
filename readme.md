#  NetworkC
This Python package written in C is a faster version of NetworkX.
I will implement the ShortestPath algorithm one after the other.

# Install
Install the latest version of NetworkC:
```bash
$ pip install git+https://github.com/atsushi-green/networkc
```

# Example
```python
import networkx as nx
import numpy as np

import networkc as nc

G = nx.DiGraph()
G.add_nodes_from(range(4))
G.add_edge(0, 0, weight=0)
G.add_edge(1, 1, weight=0)
G.add_edge(2, 2, weight=0)
G.add_edge(3, 3, weight=0)

G.add_edge(0, 1, weight=1)
G.add_edge(1, 2, weight=2)
G.add_edge(2, 3, weight=1)
G.add_edge(3, 0, weight=1)

res_c = nc.all_pairs_dijkstra_path(G, weight="weight")
res_x = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))
print(res_c == res_x)
# True
```

