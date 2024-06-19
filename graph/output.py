from networkx import DiGraph


def print_graph(graph: DiGraph, mode='all'):
    print(f'An attack graph with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges')

    if mode == 'all' or mode == 'nodes':
        print('===== Nodes =====')
        nodes = graph.nodes.data()
        for node in nodes:
            print(f'Node {node[0]} ({node[1]["name"]}), type {node[1]["_type"]}, prob {node[1]["prob"]}, '
                  f'cumulative prob {node[1]["cumulative"]:.5f}, cost {node[1]["cost"]}')
    if mode == 'all' or mode == 'edges':
        print('===== Edges =====')
        edges = graph.edges.data()
        for edge in edges:
            print(f'Edge ({edge[0]}, {edge[1]}), prob {edge[2]["prob"]}, cost {edge[2]["cost"]}')
