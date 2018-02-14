G = {}
node_num = 0
edge_num = 0


class Item:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val


class Heap:
    def __init__(self):
        self.__map = {}
        self.__data = []
        self.__size = 0

    def insert(self, item: Item):
        self.__data.append(item)
        self.__map[item.key] = len(self.__data)-1
        current_index = len(self.__data) - 1
        while current_index != 0:
            father_index = (current_index - 1) // 2
            if self.__data[father_index].val > self.__data[current_index].val:

                # swap father_index item and current_index item
                tmp = self.__data[father_index]
                self.__data[father_index] = self.__data[current_index]
                self.__data[current_index] = tmp

                # modify key index map
                self.__map[self.__data[current_index].key] = current_index
                self.__map[self.__data[father_index].key] = father_index
            current_index = father_index

    def pop_min(self) -> Item:
        min_item = self.__data[0]

        # swap last item and first(min) item, then delete last item(min item)
        self.__data[0] = self.__data[-1]
        del self.__data[-1]

        # modify key index map
        del self.__map[min_item.key]
        self.__map[self.__data[0].key] = 0

        current_index = 0
        heap_size = len(self.__data)
        while current_index*2 + 1 < heap_size:
            left_index = current_index*2 + 1
            right_index = current_index*2 + 2
            if right_index == heap_size:
                right_index = left_index
            min_child_index = left_index if self.__data[left_index].val < self.__data[right_index].val else right_index

            # swap current_index item and min_child_index item
            tmp = self.__data[min_child_index]
            self.__data[min_child_index] = self.__data[current_index]
            self.__data[current_index] = tmp

            # modify key index map
            self.__map[self.__data[min_child_index].key] = min_child_index
            self.__map[self.__data[current_index].key] = current_index
            current_index = min_child_index
        return min_item

    def get_min(self) -> Item:
        return self.__data[0]

    def size(self) -> int:
        return len(self.__data)

    def empty(self) -> bool:
        return len(self.__data) == 0

    def delete_by_item(self, item: Item) -> Item:
        return self.delete_by_key(item.key)

    def delete_by_key(self, key: int) -> Item:
        index = self.__map[key]
        delete_item = self.__data[index]

        # swap data[index] and data[-1]
        self.__data[index] = self.__data[-1]
        del self.__data[-1]

        # modify key index map
        del self.__map[delete_item.key]
        self.__map[self.__data[0].key] = index

        left_child_index = index * 2 + 1
        if left_child_index >= len(self.__data):
            left_child_index = index
        father_index = max((index-1)//2, 0)

        while self.__data[father_index].val > self.__data[index].val:

            # swap data[father_index] and data[index]
            tmp = self.__data[father_index]
            self.__data[father_index] = self.__data[index]
            self.__data[index] = tmp

            # modify key index map
            self.__map[self.__data[father_index]] = father_index
            self.__map[self.__data[index]] = index

            # update index and father_index
            index = father_index
            father_index = (index-1)//2
            if father_index < 0:
                break

        while self.__data[left_child_index].val < self.__data[index].val:

            # swap data[left_child_index] and data[index]
            tmp = self.__data[left_child_index]
            self.__data[left_child_index] = self.__data[index]
            self.__data[index] = tmp

            # modify key index map
            self.__map[self.__data[left_child_index]] = left_child_index
            self.__map[self.__data[index]] = index

            # update index and left_child_index
            index = left_child_index
            left_child_index = index * 2 + 1
            if left_child_index >= len(self.__data):
                break

        return delete_item


def prim_min_spanning_tree():
    global G
    global node_num
    global edge_num



def main():
    global G
    global node_num
    global edge_num
    heap = Heap()

    with open('edges.txt', 'r') as file:
        meta_line = file.readline()
        node_num = meta_line[0]
        edge_num = meta_line[1]
        for line in file.readlines():
            line = line.split()
            node1 = int(line[0])
            node2 = int(line[1])
            cost = int(line[2])
            if node1 not in G:
                G[node1] = {}
            if node2 not in G:
                G[node2] = {}
            G[node1][node2] = cost
            G[node2][node1] = cost


main()
