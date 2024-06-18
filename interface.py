import logging
import sys
import tkinter
from tkinter import filedialog

from utils.csv_reader import *
from graph.probability import *


def command_help():
    print('Available commands:')
    print('\033[4mv\033[0miew [nodes|edges|history] - views the nodes or edges in the graph, or the history. \n'
          'Default to view nodes and edges')
    print('\033[4mc\033[0malculate [u] - calculates the cumulative probability at u. Defaults to the goal node')
    print('\033[4md\033[0melete <u [v]> - deletes the node u or the edge (u, v). Unreachable nodes will be pruned after')
    print('\033[4mu\033[0mndo [n] - undo n actions. Defaults to 1')
    print('\033[4mr\033[0meset - reset the graph to its original state')
    print('set - configures the program, enter ?set for more info')
    print('\033[4mq\033[0muit - terminates the program')


def calculate(graph: DiGraph):
    calculate_prob(graph)
    print()


def main_loop(graph: DiGraph):
    while True:
        cmd = input('> ').split(' ')

        if len(cmd) < 1 or len(cmd[0]) < 1:
            continue

        if cmd[0] == 'v' or cmd[0] == 'view':
            print('Not implemented yet')
        elif cmd[0] == 'c' or cmd[0] == 'calculate':
            calculate(graph)
        elif cmd[0] == 'd' or cmd[0] == 'delete':
            pass
        elif cmd[0] == 'u' or cmd[0] == 'undo':
            pass
        elif cmd[0] == 'r' or cmd[0] == 'reset':
            pass
        elif cmd[0] == 'set':
            pass
        elif cmd[0] == 'q' or cmd[0] == 'quit':
            exit(0)
        elif cmd[0] == '?' or cmd[0][0] == '?':
            if len(cmd) == 1 and len(cmd[0]) == 1:
                command_help()
            if len(cmd) == 1:
                sub_cmd = cmd[0][1:]
            else:
                sub_cmd = cmd[1]
            if sub_cmd == 'set':
                pass
        else:
            print('Unrecognized command')


def start():
    print('Welcome to Attack Graph Explorer')
    print('Enter ? for command help')

    folder = ''
    if len(sys.argv) < 2:
        print('Please choose or enter a directory where attack graph is')
        try:
            tkinter.Tk().withdraw()
            folder = filedialog.askdirectory(title='Please select your attack graph directory')
        except tkinter.TclError:
            logging.warning('Tkinter encountered an error, host likely is headless')
            folder = input('')
    else:
        folder = sys.argv[1]

    print(f'\nSelected folder: {folder}')

    graph = read_graph(folder)
    print(f'Graph created from input with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges')

    if 'goal' in graph.graph:
        print(f'The goal node is {graph.graph["goal"]}')
    else:
        goal = int(input('Please enter the index of the goal node: '))
        graph.graph['goal'] = goal

    main_loop(graph)


if __name__ == '__main__':
    start()
