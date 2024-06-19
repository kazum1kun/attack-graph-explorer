import networkx
from networkx import DiGraph
from queue import Queue


# Check if node u can be pruned after removing an edge
def check_node(graph: DiGraph, u, direction):
    if direction == 'in' and graph.in_degree(u) == 1:
        return True
    if direction == 'in' and graph.nodes[u]['_type'] == 'AND':
        return True
    if direction == 'out' and graph.out_degree(u) == 1:
        return True
    return False


def delete_element(graph: DiGraph, u, v=None):
    pending = Queue()
    node_counter = 0
    edge_counter = 0

    # When v is None, it is deleting node; otherwise it deletes an edge
    if v is None:
        if graph.has_node(u):
            pending.put(u)
        else:
            return None, None
    else:
        if graph.has_edge(u, v):
            deleted = False
            if check_node(graph, u, 'out'):
                pending.put(u)
                deleted = True
            if check_node(graph, v, 'in'):
                pending.put(v)
                deleted = True
            if not deleted:
                graph.remove_edge(u, v)
                return 0, 1
        else:
            return None, None
    # Go through all nodes in pending and prune it if
    # 1) it has no outgoing edges
    # 2) it has no incoming edges
    # 3) it is an AND node, and one of its incoming edge was pruned
    while not pending.empty():
        u = pending.get()
        if not graph.has_node(u):
            continue
        for v in graph.in_edges(u):
            v = v[0]
            if check_node(graph, v, 'out'):
                pending.put(v)
        for v in graph.out_edges(u):
            v = v[1]
            if check_node(graph, v, 'in'):
                pending.put(v)
        edges_before = graph.number_of_edges()
        graph.remove_node(u)
        edges_after = graph.number_of_edges()

        node_counter += 1
        edge_counter += edges_before - edges_after
    return node_counter, edge_counter
