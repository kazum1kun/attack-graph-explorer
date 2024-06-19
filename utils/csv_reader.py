import csv
import os
import logging
import sys

from networkx import DiGraph


def read_graph(path):
    arc_file = os.path.join(path, 'ARCS.CSV')
    vert_file = os.path.join(path, 'VERTICES.CSV')
    if not os.path.exists(arc_file) or not os.path.exists(vert_file):
        logging.critical(f'ARCS.CSV or VERTICES.CSV not found in {path}')
        sys.exit(1)

    graph = DiGraph()
    goal = -99999

    with open(vert_file, 'r') as file:
        for line in csv.reader(file):
            idx = int(line[0])
            name = line[1]
            _type = line[2]
            prob = float(line[3])
            cost = float(line[4])

            graph.add_node(idx, name=name, _type=_type, prob=prob, cost=cost)

            if name == 'g' or name == 'goal':
                goal = idx

    with open(arc_file, 'r') as file:
        for line in csv.reader(file):
            src = int(line[1])
            dst = int(line[0])
            prob = float(line[2])
            cost = float(line[3])

            graph.add_edge(src, dst, prob=prob, cost=cost)

    if goal != -99999:
        graph.graph['goal'] = goal

    return graph
