#The Dijkstra Algorithm in python using the NetworkX library.

import networkx as nx
from pprint import pprint
G=nx.read_weighted_edgelist("edge_weights.csv",
create_using=nx.DiGraph(),nodetype=str)
pred, dist = nx.dijkstra_predecessor_and_distance(G, "skaigr")
sorted(pred.items())
pprint(sorted(dist.items()))