

from utils import *

graph = readIn('toyGraph.txt')

nodes, edges = graphToLists(graph)

adj = graphToAdjList(graph)

for i in adj:
    print i, adj[i]
'''
for i in nodes:
    print i

for i in edges:
    print i, graph[i[0]][i[1]]['weight']
'''

#CC = BFS(graph, 'A')
