#Graph Projection in Python using NetworkX

import networkx as nx
G=nx.read_edgelist("nxgraph.txt", create_using=nx.Graph(),nodetype=str)
from networkx.algorithms import bipartite
H,A = nx.bipartite.sets(G)
Ph = bipartite.weighted_projected_graph(G, list(A))