class Element:
    def __init__(self, start_node, end_node, value):
        self.start_node = start_node
        self.end_node = end_node
        self.value = value


# TODO 使用 heap 加速
class Heap:
    def __init__(self):
        self.__map = {}
        self.__data = []
        self.__size = 0

    def insert(self, k: Element):
        self.__data.append(k)
        current_index = len(self.__data) - 1
        while current_index != 0:
            father_index = (current_index - 1) // 2
            if self.__data[father_index].value > self.__data[current_index].value:
                tmp = self.__data[father_index]
                self.__data[father_index] = self.__data[current_index]
                self.__data[current_index] = tmp
            current_index = father_index

    def pop_min(self) -> Element:
        min_element = self.__data[0]
        self.__data[0] = self.__data[-1]
        del self.__data[-1]
        current_index = 0
        heap_size = len(self.__data)
        while current_index*2 + 1 < heap_size:
            left_index = current_index*2 + 1
            right_index = current_index*2 + 2
            if right_index == heap_size - 1:
                right_index = left_index
            min_child_index = left_index if self.__data[left_index].value < self.__data[right_index].value else right_index
            tmp = self.__data[min_child_index]
            self.__data[min_child_index] = self.__data[current_index]
            self.__data[current_index] = tmp
            current_index = min_child_index
        return min_element

    def get_min(self) -> int:
        return self.__data[0]

    def empty(self) -> bool:
        return len(self.__data) == 0


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


main()
