import networkx as nx
import random 

G = nx.DiGraph()
n = 100

for i in range(n): 
    G.add_node(i)

''' give random probabilities to every else edge  '''
P = []
for i in range(n):
    r = random.uniform(0,.25)
    P.append(r)

''' forming rest of the graph '''
for i in range(n):
    for j in range(n):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)

''' form a coalition '''
 
cluster = []
A = list(G.nodes()) 
a = len(A)
while(len(cluster) < 20 ):
    cluster.append(random.choice(A))

for i in cluster:
    for j in cluster:
        if(i!=j):
            G.add_edge(i,j)

def edge_to_remove(G) :
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = dict1.items()
    list = sorted(list_of_tuples, key = lambda x:x[1], reverse= True)
    return list[0][0]

def girvan(G):
    l = nx.number_connected_components(G)
    print ('components : '+str(l))

    while( l < a-len(cluster)+1):
        G.remove_edge(*edge_to_remove(G))
        l = nx.number_connected_components(G)
        print('components : '+str(l))
    c = list(nx.connected_components(G))
    return c


H = G.to_undirected()
c = girvan(H)
print(c)

def modularity(coalition):
    m = G.number_of_edges()
    sum = 0
    if(len(coalition) == 1):
        return sum

    for i in coalition:
        for j in coalition:
            if((i!=j) & (G.has_edge(i,j)) & (m!=0) ):
                ki_in = G.subgraph(coalition).in_degree(i)
                kj_out = G.subgraph(coalition).out_degree(j)
                sum = sum + (1-((ki_in)*(kj_out)/m))/m
            if((i!=j) & (G.has_edge(i,j) == False ) & (m!=0) ):
                ki_in = G.subgraph(coalition).in_degree(i)
                kj_out = G.subgraph(coalition).out_degree(j)
                sum = sum - ((ki_in)*(kj_out)/(m*m))    
    return sum            


modularities = []
for i in range(len(c)):
    modularities.append(modularity(c[i]))


print(max(c,key=len))
print(cluster,len(cluster))
print(modularity(cluster))