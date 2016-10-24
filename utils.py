
import random


def readIn(filename):
    File = open(filename, 'r')
    data = File.read()
    File.close()
    data = data.split('\n')
    header = data.pop(0)
    data.pop()
    header = header.split(',')
    dic = {}
    for i in range(len(data)):
        row = data[i].split(',')
        if row[0] in dic:
            if not(row[1] in dic[row[0]].keys()):
                dic[row[0]][row[1]] = {}
            if len(header) > 2:
                for j in range(2,len(header)):
                    dic[row[0]][row[1]][header[j]] = row[2]
        else:
            dic[row[0]] = {row[1]:{}}
            if len(header) > 2:
                    for j in range(2,len(header)):
                        dic[row[0]][row[1]][header[j]] = row[2]
    return dic


def graphToLists(graph, direc = False):
    nodes = []
    edges = []
    for i in graph:
        if not(i in nodes):
            nodes.append(i)
        for j in graph[i]:
            if not(j in nodes):
                nodes.append(j)
            if not([i,j] in edges) or (direc and not([j,i] in edges)):
                edges.append([i,j])
    return nodes, edges


def graphToAdjList(graph):
    dic = {}
    for i in graph:
        for j in graph[i]:
            if i in graph:
                if not(j in graph[i]):
                    graph[i].append(j)
            else :
                graph[i] = [j]

            if j in graph:
                if not(i in graph[j]):
                    graph[j].append(i)
            else :
                graph[j] = [i]


def BFS(graph, s = None):
    graph = graphToAdjList(graph)
    if s == None:
        s = graph.keys()[0]
    visited = [s]
    Q = [s]
    while len(Q) > 0:
        w = Q.pop()
        neighbors = graph[w]
        for i in neighbors:
            if not(i in visited):
                visited.append(i)
                Q.append(i)
    return visited


def find_largest_cc(graph):
    nodes = graph.keys()
    largest = 0
    conComp = []
    while len(nodes) > 0:
        temp = BFS(graph, nodes[0])
        if largest < len(temp):
            largest = len(temp)
            conComp = temp
        for i in temp:
            nodes.remove(i)
    out = {}
    for i in conComp:
        out[i] = graph[i]
    return out


def getRanEdge(graph, seed = False):
    if seed:
        random.seed(5311995)
    tail = random.choice(graph.keys())
    head = randome.choice(graph[tail].keys())
    return [tail,head]


def getRanNode(graph, seed = False):
    if seed:
        random.seed(5311995)
    nodes = []
    for i in graph:
        if not(i in nodes):
            nodes.append(i)
        for j in graph[i]:
            if not(j in nodes):
                nodes.append(j)
    return random.choice(nodes)
