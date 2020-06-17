import networkx as nx
import numpy as np
import random 

G = nx.DiGraph()
F = nx.DiGraph()
n = 15

for i in range(n): 
    G.add_node(i)

''' give random probabilities to every else edge  '''
P = []
for i in range(n):
    r = random.uniform(0,.25)
    P.append(.25)
''' forming rest of the graph '''

for i in range(n):
    for j in range(n):
        if(i!=j):
            k = random.uniform(0,1)
            if(k<P[i]):
                G.add_edge(j,i)

upvote_normal = []
upvote_cluster = []

for i in range(n):
    upvote_normal.append(len(G.in_edges(i)))

J = G.to_undirected()
C = []
for i in J:
    C.append(J.degree(i))
counter2 = sum(C)

clusters_normal = []
for i in range(n):
    clusters_normal.append(i//3)
'print(clusters_normal)'    
def di2(m):
    c = 0
    for i in J:
        if((i in J.neighbors(m)) & (clusters_normal[i] == clusters_normal[m])):
            c = c+1
    return c  

def ti2(m):
    a = []
    sol = 0
    for i in J:
        if((i in J.neighbors(m)) & (clusters_normal[i] == clusters_normal[m])):
            a.append(i)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if(a[j] in J.neighbors(a[i])):
                sol = sol+1
    return sol           

def utility_normal(m):
    if(di2(m) == 0):
        ut = 0
    elif(di2(m) == 1):
        ut = di2(m)
    elif(di2(m)>1):
        ut = (di2(m))+(2*ti2(m)/(di2(m)-1))    
    return ut    
    
util_normal = []
for i in range(n):
    util_normal.append(utility_normal(i))


Q = sorted(range(len(C)), key=lambda k: C[k])
'print(Q)'

while(1>0):
    count = 0
    for i in Q:
        for j in J.neighbors(i):
            u1_normal = util_normal[i]
            temp1 = clusters_normal[i]
            clusters_normal[i] = clusters_normal[j]
            u2_normal = utility_normal(i)
            if(u2_normal>u1_normal):
                util_normal[i] = u2_normal
            else:
                clusters_normal[i] = temp1
                count = count+1 
    if(count == counter2):
        break   
'print(clusters_normal)'  
print(upvote_normal)
for i in range(n):
    util_normal[i] = round(util_normal[i])              
'print(util_normal)'


cluster = [0,1,2,3,4,5]
'''
for i in range(33):
    cluster.append(i)
'''
A = list(G.nodes()) 
a = len(A)

for i in cluster:
    for j in cluster:
        if(i!=j):
            G.add_edge(i,j)
'''
#another cluster
cluster1 = []
for i in range (66,99):
    cluster1.append(i)

for i in cluster1:
    for j in cluster1:
        if(i!= j):
            G.add_edge(i,j)     
'''
for i in range(n):
    upvote_cluster.append(len(G.in_edges(i)))
'print(upvote_normal)'
'print(upvote_cluster)'
H = G.to_undirected()
B = []
for i in H:
    B.append(H.degree(i))
counter = sum(B)

clusters = []
for i in range(n):
    clusters.append(i//3)
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
for s in range(n):
    util.append(utility(s))


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

'print(clusters)'
print(upvote_cluster)
for i in range(n):
    util[i] = round(util[i])
print(util_normal)
print(util)

credit_score_normal = []
credit_score_cluster = []

for i in range(n):
    credit_score_normal.append(0)
    credit_score_normal[i] = upvote_normal[i] - util_normal[i]
    credit_score_normal[i] = n + credit_score_normal[i]

for i in range(n):
    credit_score_cluster.append(0)
    credit_score_cluster[i] = upvote_cluster[i] - util[i]
    credit_score_cluster[i] = n + credit_score_cluster[i]

print(credit_score_normal)
print(credit_score_cluster)

sum1,sum5,sum6=0,0,0
sum2=0
sum3=0
sum4=0

'''
for i in cluster:
    sum1 = sum1 + (credit_score_normal[i])
for i in G.nodes():
    if i not in cluster:
        if i not in cluster1:
            sum2 = sum2 + (credit_score_normal[i])
for i in cluster1:
    sum3 = sum3 + (credit_score_normal[i])            
print(sum1/len(cluster),sum2/(n - len(cluster) - len(cluster1)),sum3/len(cluster1))

for i in cluster:
    sum4 = sum4 + (credit_score_cluster[i])
for i in G.nodes():
    if i not in cluster:
        if i not in cluster1:
            sum5 = sum5 + (credit_score_cluster[i])
for i in cluster1:
    sum6 = sum6 + credit_score_cluster[i]            
print(sum4/len(cluster),sum5/(n - len(cluster) - len(cluster1)),sum6/len(cluster1))
'''
for i in cluster:
    sum1 = sum1 + (credit_score_normal[i])
for i in G.nodes():
    if i not in cluster:
      sum2 = sum2 + (credit_score_normal[i])
for i in cluster:
    sum3 = sum3 + (credit_score_cluster[i])
for i in G.nodes():
    if i not in cluster:
      sum4 = sum4 + (credit_score_cluster[i])
print(sum1/len(cluster),sum2/(n - len(cluster)))
print(sum3/len(cluster),sum4/(n - len(cluster)))
'''
for i in cluster:
    sum5 = sum5 + (util[i])
for i in range(n):
    if i not in cluster:
        sum6 = sum6 + (util[i])

print(sum5/len(cluster),sum6/(n - len(cluster)))
'''