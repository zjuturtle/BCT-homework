class Element:
    def __init__(self, start_node, end_node, value):
        self.start_node = start_node
        self.end_node = end_node
        self.value = value


# TODO use heap to speed up

G = {}
node_max_index = 0


def dijkstra(s: int):
    global G
    global node_max_index

    # 初始化
    A = [1000000] * (node_max_index+1)
    A[s] = 0
    X = set([s])

    while len(X) != len(G):
        w_star = -1
        min_vw = 1000000
        for v in X:
            for w, lvw in G[v].items():
                if w in X:
                    continue
                if A[v] + lvw < min_vw:
                    min_vw = A[v] + lvw
                    w_star = w
        X.add(w_star)
        A[w_star] = min_vw

    print(str(A[7])+',' +
          str(A[37])+',' +
          str(A[59]) + ',' +
          str(A[82]) + ',' +
          str(A[99]) + ',' +
          str(A[115]) + ',' +
          str(A[133]) + ',' +
          str(A[165]) + ',' +
          str(A[188]) + ',' +
          str(A[197]))


def main():
    global G
    global node_max_index

    with open('dijkstraData.txt', 'r') as graph_file:
        while True:
            lines = graph_file.readlines(200)
            if not lines:
                break
            for line in lines:
                line = line.split()
                start_node = int(line[0])
                if start_node not in G:
                    G[start_node] = {}
                for index in range(1, len(line)):
                    edge = line[index].split(sep=',')
                    end_node, length = [int(edge[0]), int(edge[1])]
                    G[start_node][end_node] = length
                    if end_node not in G:
                        G[end_node] = {}

                    node_max_index = max(node_max_index, start_node, end_node)
    dijkstra(1)


if __name__ == "__main__":
    main()
