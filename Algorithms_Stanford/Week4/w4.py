from typing import Set


class Node:
    def __init__(self, index: int, out_edge: Set[int]):
        self.index = index
        self.out_edge = out_edge


class Graph:
    def __init__(self):
        self.nodes = set()


G_list = []
G = Graph()


def main():
    global G_list
    global G

    with open('kargerMinCut.txt', 'r') as graph_file:
        while True:
            lines = graph_file.readlines(300)
            if not lines:
                break
            for line in lines:
                tmp = []
                for x in line.split():
                    tmp.append(int(x))
                G_list.append(tmp[1:-1])
                G.nodes.add(Node(index=tmp[0], out_edge=set(tmp[1:-1])))
    print(G_list)


main()
