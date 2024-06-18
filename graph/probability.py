from networkx import DiGraph
from queue import Queue


def calculate_prob(graph: DiGraph):
    ready = Queue()
    nodes = graph.nodes

    for node in nodes:
        if nodes[node]['_type'] == 'LEAF':
            nodes[node]['cumulative'] = nodes[node]['prob']
            ready.put(node)
        else:
            nodes[node]['done'] = 0
            nodes[node]['cumulative'] = 1

    while not ready.empty():
        curr = ready.get()
        for adj in graph[curr]:
            temp = nodes[curr]['cumulative'] * graph[curr][adj]['prob']
            if nodes[adj]['_type'] == 'OR':
                if nodes[adj]['done'] == 0:
                    nodes[adj]['cumulative'] = temp
                    nodes[adj]['fail'] = 1 - temp
                else:
                    nodes[adj]['cumulative'] = (1 - nodes[adj]['fail'] * (1 - temp))
                    nodes[adj]['fail'] *= 1 - temp
            elif nodes[adj]['_type'] == 'AND':
                nodes[adj]['cumulative'] *= temp

            nodes[adj]['done'] += 1
            if nodes[adj]['done'] == graph.in_degree(adj):
                nodes[adj]['cumulative'] *= nodes[adj]['prob']
                ready.put(adj)
