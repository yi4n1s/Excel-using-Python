#Script 6: The Girvan - Newman Algorithm in Python using NetworkX

import networkx as nx
import matplotlib.pyplot as plt

def edge_to_remove(G):
	dict1 = nx.edge_betweenness_centrality(G)
	list_of_tuples = list(dict1.items())
	list_of_tuples.sort(key = lambda x: x[1], reverse = True)
	return list_of_tuples[0][0] #(a,b)

def girvan(G):
	c = list(nx.connected_component_subgraphs(G))
	#l = sum(1 for x in c)
	l = len(c)
	print("The number of connected components are ", l)
	
	while (l < 7):
		G.remove_edge(*edge_to_remove(G))#((a,b)) --> (a,b)
		c = list(nx.connected_component_subgraphs(G))
		#l = sum(1 for x in c)
		l = len(c)
		print("The number of connected components are ", l)
	return c
G = nx.read_edgelist("hub-hub.csv", create_using=nx.Graph(),nodetype=str)
c = girvan(G)

for i in c:
	print(i.nodes())
	print(".............")
	#nx.draw_spring(i)
	#plt.show()

#GN = nx.disjoint_union(c[0],c[1])
#print("Union............")
#nx.draw_spring(GN)
#plt.show()