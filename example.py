

from utils import *

graph = readIn('toyGraph.txt')

nodes, edges = graphToLists(graph)

print 'Nodes:'
for i in nodes:
    print i
print
print 'Edges and weight:'

for i in edges:
    print str(i) + ':', graph[i[0]][i[1]]['weight'] + '\n'
print

print 'Adjacency lists'
adj = graphToAdjList(graph)

for i in nodes:
    print i + ':' ,adj[i]
print


CC = BFS(graph, 'G')

LCC = find_largest_cc(graph)
print 'Largest Connected Component\n'
print LCC
print

print 'Ten Random Edges'
for i in range(10):
    print getRanEdge(graph)
print

print 'Ten Random Nodes'
for i in range(10):
    print getRanNode(graph)
