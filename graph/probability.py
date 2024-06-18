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
        u = ready.get()
        for v in graph[u]:
            temp = nodes[u]['cumulative'] * graph[u][v]['prob']
            if nodes[v]['_type'] == 'OR':
                if nodes[v]['done'] == 0:
                    nodes[v]['cumulative'] = temp
                    nodes[v]['fail'] = 1 - temp
                else:
                    nodes[v]['cumulative'] = (1 - nodes[v]['fail'] * (1 - temp))
                    nodes[v]['fail'] *= 1 - temp
            elif nodes[v]['_type'] == 'AND':
                nodes[v]['cumulative'] *= temp

            nodes[v]['done'] += 1
            if nodes[v]['done'] == graph.in_degree(v):
                nodes[v]['cumulative'] *= nodes[v]['prob']
                ready.put(v)
