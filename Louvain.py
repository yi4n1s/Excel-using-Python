#The Louvain Algorithm in Python using NetworkX

import community
import networkx as nx
G=nx.read_edgelist("hub-user.csv", create_using=nx.Graph(),nodetype=str)
partition = (community.best_partition(G))
pprint(partition)