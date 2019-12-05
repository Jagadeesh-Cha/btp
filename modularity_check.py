import networkx as nx
import random 
from itertools import combinations

''' number of nodes = 7 '''

G = nx.DiGraph()
n = 7

for i in range(n): 
    G.add_node(i)

print("nodes: " + str(G.nodes()))

''' give random probabilities to every else edge  '''
P = []
for i in range(n):
    r = random.uniform(0,.25)
    P.append(r)
print(P)

''' forming rest of the graph '''
for i in range(n):
    for j in range(n):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)

''' coalition : [1,2,4] ''' 
cluster = [1,2,4]
for i in cluster:
    for j in cluster:
        if(i!=j):
            G.add_edge(i,j)


print(G.number_of_edges())

''' modularity function for a coalition '''

def modularity(coalition):
    m = G.number_of_edges()
    remaining = []
    sum = 0
    P_sum = prob_sum(coalition)
    if(len(coalition) == 1):
        return sum

    for i in coalition:
        for j in coalition:
            if((i!=j) & (G.has_edge(i,j)) & (m!=0) ):
                ki_in = G.subgraph(coalition).in_degree(i)
                kj_out = G.subgraph(coalition).out_degree(j)
                '''ki_in = P[i]*(len(coalition)-1)
                kj_out = P_sum - P[j]''' 
                sum = sum + (1-((ki_in)*(kj_out)/m))/m
            if((i!=j) & (G.has_edge(i,j) == False ) & (m!=0) ):
                ki_in = G.subgraph(coalition).in_degree(i)
                kj_out = G.subgraph(coalition).out_degree(j)
                '''ki_in = P[i]*(len(coalition)-1)
                kj_out = P_sum - P[j]'''                
                sum = sum - ((ki_in)*(kj_out)/(m*m))    
    '''remaining = G.nodes() - coalition
    for l in remaining:
        kl_in = G.in_degree(l)
        kl_out = G.out_degree(l)
        sum = sum - ((kl_in)*(kl_out)/(m*m))'''
    return sum            

''' find the modularities for all coalitions '''
N = G.nodes()
modularities = []
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

def prob_sum(coalition):
    sum = 0
    length = len(coalition)
    for i in range(length):
        sum = sum + P[coalition[i]]
    return sum    

'''print(sub_lists(N))'''
for i in range(1,len(sub_lists(N))):
    modularities.append(modularity(sub_lists(N)[i]))

'''print(modularities)'''
''' finding maximum in this modularities ''' 
maximum = modularities.index(max(modularities))
print(sub_lists(N)[maximum+1])

print(G.edges())
