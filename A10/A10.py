#Project    : Algorithms - Activity 10
#Developer: : Dago Quevedo
#Date       : Jan 20

import random
import math
import sys
import networkx as nx
import matplotlib.pyplot as plt

class graph:
    #Init class
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

            self.E[i,j] = round(random.uniform(0,1)) if (j,i) not in self.E.keys() else self.E[j,i]
                
        self.dist()
        self.grad()
        
    #Density
    def dens(self):
        n = len(self.V)
        m = sum(self.E.values()) / 2.0
        dens = m / ((n * (n - 1))/ 2.0)

        return dens
        
    #Distance
    def dist(self):
        for s in self.V:
            K = self.dijkstra(s)
            for t in K.keys():
                self.D[s,t] = K[t] if K[t] != math.inf else 0
         
    #Grade
    def grad(self):
        for i in self.V:
            self.G[i] = sum([self.E[i,j] for j in self.V])
    
    #Diameter
    def diam(self):
        return max(self.D.values())

    #Dijkstra algorithm
    def dijkstra(self,s):
        d = {}
        v = {}
        for w in self.V:
            v[w] = 0
            d[w] = math.inf if self.E[s,w] == 0 else 1

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

    #Depth-First Search
    def dfs(self, v, L):
        L.append(v)
        for w in [j for j in self.V if self.E[v,j] == 1]:
            dfs(w,L)
            
        return L

    
    #plot object
    def plot(self,show):
        g_plot = nx.Graph()
        for i in G.V:
            g_plot.add_node(i)
        for (i,j) in G.E:
            if G.E[i,j] == 1:
                g_plot.add_edge(i,j)
        
        nx.draw(g_plot,with_labels = True)
        
        if(show):
            plt.show()

        plt.savefig('graph_out.png')


if __name__== '__main__':
    if len(sys.argv) < 2:
        print('Failed operation, a number of nodes are expected')
        sys.exit()
    
    G = graph(int(sys.argv[1]))

    print('Diameter: %d' % G.diam())
    print('Density: %4.2f' % G.dens())
        
    print('Node with the minimum centrality: %d' % min(G.G, key=G.G.get))
    print('Node with the maximum centrality: %d' % max(G.G, key=G.G.get))
        
    G.plot(True)
