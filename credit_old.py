import networkx as nx
import random 
from itertools import combinations

''' number of nodes = 7 '''

G = nx.DiGraph()
n = 15

for i in range(n): 
    G.add_node(i)

print("nodes: " + str(G.nodes()))

''' give random probabilities to every else edge  '''
P = []
for i in range(n):
    P.append(.25)
'''print(P)'''

''' forming rest of the graph '''
for i in range(n):
    for j in range(n):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)

''' coalition : [1,2,4] ''' 
cluster = [0,1,2,3,4,5]
for i in cluster:
    for j in cluster:
        if(i!=j):
            G.add_edge(i,j)


print(cluster)
m = G.number_of_edges()

''' modularity function for a coalition '''

def modularity(coalition):
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
                #ki_in = P[i]*(len(coalition)-1)
                #kj_out = P_sum - P[j] 
                sum = sum + (1-((ki_in)*(kj_out)/m))/m
            if((i!=j) & (G.has_edge(i,j) == False ) & (m!=0) ):
                ki_in = G.subgraph(coalition).in_degree(i)
                kj_out = G.subgraph(coalition).out_degree(j)
                #ki_in = P[i]*(len(coalition)-1)
                #kj_out = P_sum - P[j]                
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
maxmod = max(modularities)
sol = sub_lists(N)[maximum+1]
print(sol)
print(maxmod)
for i in range(n):
    if(i not in sol):
        maxmod = maxmod + ((G.in_degree(i) * G.out_degree(i))/(m*m))
print(maxmod)
'''
def ind_mod(t):
    sol = 0
    for i in range(n):
        if(G.has_edge(t,i)):
            sol = sol + (1-(G.in_degree(t)*G.out_degree(i)/m))/m
        elif(G.has_edge(t,i) == False):
            sol = sol - (G.in_degree(t)*G.out_degree(i)/(m*m)) 
        return sol       
'''
# credit scores of players
credit_score = []
for i in range(n):
    credit_score.append(0)
for i in range(n):
    if i in sol:
        mod = maxmod
        #beta = 2*n*n*(n-1)*(n-1)*(1-P[i])/((n-3)*(min(P)))
        credit_score[i] = G.in_degree(i) - mod*n
    elif i not in sol:
        mod = (G.in_degree(i) * G.out_degree(i))/(m*m)
        #beta = 2*n*n*(n-1)*(n-1)*(1-P[i])/((n-3)*(min(P)))
        credit_score[i] = G.in_degree(i) + mod*n
ins = []
for i in range(n):
    ins.append(G.in_degree(i))
print(ins)    
for i in range(n):
    credit_score[i] = round(credit_score[i],2)
print(credit_score)        
T = []
for i in range(n):
    if i in sol:
        T.append(maxmod)
    elif i not in sol:
        T.append(-(G.in_degree(i) * G.out_degree(i))/(m*m))    
print(T)        