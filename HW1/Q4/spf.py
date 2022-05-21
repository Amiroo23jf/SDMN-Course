import networkx as nx
import numpy as np

def spf(A):
    n = A.shape[0]
    
    # creating the graph according to the given Matrix
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

    # finding the shortest path
    ## we calculate x+1 because the indexing of the output of the nx.dijkstra_path() starts from 0 to n-1
    ## however, the indexing of our switches is from 1 to n
    spf_1_n = [x+1 for x in nx.dijkstra_path(G, 0, n-1)]
    spf_n_1 = [x+1 for x in nx.dijkstra_path(G, n-1, 0)]

    return (spf_1_n, spf_n_1)

    
