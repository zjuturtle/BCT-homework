import gzip
import shutil

f_rev = {}  # 与课程中相反
G = {}
G_rev = {}
G_explored = {}
G_rev_explored = {}
nodeIndexMax = 0
nodeIndexMin = 999999999
t = 0
finish = []


def dfs_rev(i):
    """
    在 G_rev 上非递归版本的 DFS，为了得到正确的 f_rev 可能需要多次访问同一个节点
    :param i: 开始节点
    :return:
    """
    global t
    global f_rev
    global G_rev
    global G_rev_explored
    global finish
    node_stack = []

    if i in G_rev:
        node_stack.append(i)
        while bool(node_stack):
            current_node = node_stack[-1]
            G_rev_explored[current_node] = True
            next_node = -1
            for n in G_rev[current_node]:
                if G_rev_explored[n]:
                    continue
                node_stack.append(n)
                next_node = n
            if next_node == -1:
                node_stack.pop()
                if not finish[current_node]:
                    t += 1
                    f_rev[t] = current_node
                    finish[current_node] = True


def dfs_loop_rev():
    global t
    global G_rev
    global G_rev_explored
    global nodeIndexMin
    global nodeIndexMax
    for i in range(nodeIndexMax, nodeIndexMin-1, -1):
        if G_rev_explored[i]:
            continue
        else:
            dfs_rev(i)


def dfs(i)->int:
    """
    在 G 上非递归版本的dfs
    :param i:开始节点
    :return:能找到的节点数目
    """
    global t
    global f_rev
    global G
    global G_explored
    node_stack = []
    node_num = 0
    if i in G:
        node_stack.append(i)
        while bool(node_stack):
            current_node = node_stack.pop()
            if not G_explored[current_node]:
                G_explored[current_node] = True
                node_num += 1
                for n in G[current_node]:
                    if not G_explored[n]:
                        node_stack.append(n)
    return node_num


def dfs_loop():
    global t
    global G
    global G_explored
    global nodeIndexMax
    global nodeIndexMin
    max_size = [0, 0, 0, 0, 0]
    for i in range(nodeIndexMax - nodeIndexMin + 1, 0, -1):
        if not G_explored[f_rev[i]]:
            max_size.append(dfs(f_rev[i]))
            max_size = sorted(max_size, reverse=True)[0:-1]
    return max_size


def main():
    global G
    global G_explored
    global G_rev
    global G_rev_explored
    global nodeIndexMax
    global nodeIndexMin
    global finish

    # 解压 SCC.txt 文件
    with gzip.open('SCC.txt.gz', 'rb') as read, open('SCC.txt', 'wb') as write:
        shutil.copyfileobj(read, write)

    with open('SCC.txt', 'r') as graph_file:
        while True:
            lines = graph_file.readlines(5000)
            if not lines:
                break
            for line in lines:
                line = line.split()
                line = [int(line[0]), int(line[1])]
                if not line[0] in G:
                    G[line[0]] = {}
                if not line[1] in G_rev:
                    G_rev[line[1]] = {}
                if not line[1] in G:
                    G[line[1]] = {}
                if not line[0] in G_rev:
                    G_rev[line[0]] = {}
                G[line[0]][line[1]] = True
                G_rev[line[1]][line[0]] = True
                G_explored[line[0]] = False
                G_explored[line[1]] = False
                G_rev_explored[line[0]] = False
                G_rev_explored[line[1]] = False
                nodeIndexMax = max(line[0], nodeIndexMax)
                nodeIndexMax = max(line[1], nodeIndexMax)
                nodeIndexMin = min(line[0], nodeIndexMin)
                nodeIndexMin = min(line[1], nodeIndexMin)
    finish = [False] * (nodeIndexMax+1)
    dfs_loop_rev()
    print('{0}'.format(','.join(map(str, dfs_loop()))))


if __name__ == "__main__":
    main()
