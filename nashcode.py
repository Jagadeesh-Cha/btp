import networkx as nx
import random 

G = nx.DiGraph()
n = 99

for i in range(n): 
    G.add_node(i)

''' give random probabilities to every else edge  '''
P = []
for i in range(n):
    r = random.uniform(0,.25)
    P.append(r)

''' forming rest of the graph '''
'''
for i in range(n//3):
    for j in range(n//3):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)

for i in range((n//3)+1,2*n//3):
    for j in range((n//3)+1,2*n//3):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)

for i in range((2*n//3)+1,n):
    for j in range((2*n//3)+1,n):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)
'''
for i in range(n):
    for j in range(n):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)
                
cluster = []
A = list(G.nodes()) 
a = len(A)
for i in range (25):
    cluster.append(i)
print(cluster)

for i in cluster:
    for j in cluster:
        if(i!=j):
            G.add_edge(i,j)

H = G.to_undirected()
B = []
for i in H:
    B.append(H.degree(i))
counter = sum(B)

clusters = []
for i in range(n):
    clusters.append(i//3)
print(clusters)    
def di(m):
    c = 0
    for i in H:
        if((i in H.neighbors(m)) & (clusters[i] == clusters[m])):
            c = c+1
    return c  

def ti(m):
    a = []
    sol = 0
    for i in H:
        if((i in H.neighbors(m)) & (clusters[i] == clusters[m])):
            a.append(i)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if(a[j] in H.neighbors(a[i])):
                sol = sol+1
    return sol           

def utility(m):
    if(di(m) == 0):
        ut = 0
    elif(di(m) == 1):
        ut = di(m)
    elif(di(m)>1):
        ut = (di(m))+(2*ti(m)/(di(m)-1))    
    return ut    
    
util = []
for i in range(n):
    util.append(utility(i))


P = sorted(range(len(B)), key=lambda k: B[k])
'print(P)'

while(1>0):
    count = 0
    for i in P:
        for j in H.neighbors(i):
            u1 = util[i]
            temp = clusters[i]
            clusters[i] = clusters[j]
            u2 = utility(i)
            if(u2>u1):
                util[i] = u2
            else:
                clusters[i] = temp
                count = count+1 
    if(count == counter):
        break               

print(clusters)
print(util)
avg1=0
avg2 =0 
for i in range(25):
    avg1 = avg1+util[i]
print (avg1/25)    
for i in range(25,99):
    avg2 = avg2+util[i]
print (avg2/75)    