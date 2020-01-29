#Project    : Algorithms - Activity 1
#Developer: : Dago Quevedo
#Date       : Jan 20

import random
import math

class graph:
    def __init__(self,m):
        self.m = m
        self.V = list(range(0,self.m))
        self.E = {}
        self.D = {}
        self.G = {}

        for (i,j) in [(a,b) for a in self.V for b in self.V]:
            if i == j:
                self.E[i,j] = 0
                continue

            if (j,i) not in self.E.keys():
                self.E[i,j] = round(random.uniform(0,1))
            else:
                self.E[i,j] = self.E[j,i]
                
        self.dist()
        self.grad()
        
    def dens(self):
        n = len(self.V)
        m = sum(self.E.values()) / 2.0
        dens = m / ((n * (n - 1))/ 2.0)

        return dens
        
    def dist(self):
        for s in self.V:
            K = self.dijkstra(s)
            for t in K.keys():
                self.D[s,t] = K[t] if K[t] != math.inf else 0
                
    def grad(self):
        for i in self.V:
            self.G[i] = sum([self.E[i,j] for j in self.V])
            
    def diam(self):
        return max(self.D.values())

    def dijkstra(self,s):
        d = {}
        v = {}
        for w in self.V:
            v[w] = 0
            if self.E[s,w] == 0:
                d[w] = math.inf
            else:
                d[w] = 1
                
        d[s] = 0
        v[s] = 1
        
        while sum(v.values()) < len(v):
            min_val = math.inf
            min_key = None
            for j in self.V:
                if v[j] == 0:
                    if d[j] <= min_val:
                        min_val = d[j]
                        min_key = j
                
            q = min_key
            if q != None:
                v[q] = 1
                for y in [j for j in self.V if self.E[q,j] == 1]:
                    if d[y] > d[q] + 1:
                       d[y] = d[q] + 1
        
        return d

#Main
if __name__== '__main__':
    #parameter
    
    G = graph(5)

    print('Diameter: %d' % G.diam())
    print('Density: %4.2f' % G.dens())
    
    print('Node with the minimum centrality: %d' % min(G.G, key=G.G.get))
    print('Node with the maximum centrality: %d' % max(G.G, key=G.G.get))
    
