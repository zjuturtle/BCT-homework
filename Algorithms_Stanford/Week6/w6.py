G = {}


def dijkstra(s: int):
    global G


def main():
    global G
    with open('dijkstraData.txt', 'r') as graph_file:
        while True:
            lines = graph_file.readlines(200)
            if not lines:
                break
            for line in lines:
                line = line.split()
                start_node = int(line[0])
                if not start_node in G:
                    G[start_node] = {}
                for index in range(1, len(line)):
                    edge = line[index].split(sep=',')
                    end_node, length = [int(edge[0]), int(edge[1])]
                    G[start_node][end_node] = length


main()
