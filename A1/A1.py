#Project    : Activity 1 - Algorithms
#Developer: : Dago Quevedo
#Date       : Jan 20

import random
import math

#density
def dens(G):
    V = G[0]
    E = G[1]
    n = len(V)
    m = sum(G[1].values())/2
    dens = m / ((n * (n - 1)) / 2.0)

    return dens

#distance
def dist(G):
    d = {}
    for s in G[0]:
        K = dijkstra(G,s)
        for t in K.keys():
            d[s,t] = K[t] if K[t] != math.inf else 0

    return d

#Dijkstra algorithm
def dijkstra(G,s):
    d = {}
    v = {}
    V = G[0]
    E = G[1]
    for w in V:
        v[w] = 0
        if E[s,w] == 0:
            d[w] = math.inf
        else:
            d[w] = 1
            
    d[s] = 0
    v[s] = 1
    
    while sum(v.values()) < len(v):
        min_val = math.inf
        min_key = None
        for j in V:
            if v[j] == 0:
                if d[j] <= min_val:
                    min_val = d[j]
                    min_key = j
            
        q = min_key
        if q != None:
            v[q] = 1
            for y in [j for j in V if E[q,j] == 1]:
                if d[y] > d[q] + 1:
                   d[y] = d[q] + 1
    
    return d

#Grade
def grad(G):
    g = {}
    E = G[1]
    for i in G[0]:
        g[i] = sum([E[i,j] for j in V])

    return g

#Diameter
def diam(G):
    d = dist(G)
    return max(d.values())

#Main
if __name__== '__main__':
    #parameter
    M = 50
    
    V = list(range(0,M))
    E = {}
    
    for (i,j) in [(a,b) for a in V for b in V]:
        if i == j:
            E[i,j] = 0
            continue
    
        if (j,i) not in E.keys():
            E[i,j] = round(random.uniform(0,1))
        else:
            E[i,j] = E[j,i]
        
    G = (V,E)

    print('Diameter: %d' % diam(G))
    print('Density: %4.2f' % dens(G))
    c = grad(G)
    print('Node with the minimum centrality: %d' % min(c, key=c.get))
    print('Node with the maximum centrality: %d' % max(c, key=c.get))
    
