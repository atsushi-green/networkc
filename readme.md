#  NetworkC


# Install
Install the latest version of NetworkC:
```bash
$ pip install git+https://github.com/atsushi-green/networkc
```

# Example
```python
import networkc as nc
import networkx as nx
import numpy as np

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

weight_matrix = nx.to_numpy_array(G, weight="weight", nonedge=np.inf).tolist()
print(nc.floyd_warshall(weight_matrix))