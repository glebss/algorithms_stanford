import sys, resource
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))
from tqdm import tqdm

T, S = 0, None
leader, f_list = {}, {}

def read_arr(arr_path):
    d = {}
    with open(arr_path, 'r') as f:
        data = f.readlines()
    data = [f.strip() for f in data]
    for el in tqdm(data):
        k, v = el.split()
        d.setdefault(int(k), [])
        d[int(k)].append(int(v))
    return d

def get_reversed_graph(graph):
    d = {}
    for k, vertices in tqdm(graph.items()):
        for v in vertices:
            d.setdefault(v, [])
            d[v].append(k)
    return d

def get_new_graph(graph):
    global f_list
    d = {}
    for k, vertices in tqdm(graph.items()):
        new_k = f_list[k]
        d.setdefault(new_k, [])
        for v in vertices:
            d[new_k].append(f_list[v])
    return d

def DFS(graph, i, vertices_explored):
    global S, T, f_list
    vertices_explored.add(i)
    if second:
        leader.setdefault(S, [])
        leader[S].append(i)
    if graph.get(i):
        for w in graph[i]:
            if w not in vertices_explored:
                DFS(graph, w, vertices_explored)
    T += 1
    f_list[i] = T

def DFS_loop(graph, n_vertices=875714):
    global S
    vertices_explored = set()
    for i in tqdm(range(n_vertices, 0, -1)):
        if i not in vertices_explored:
            S = i
            DFS(graph, i, vertices_explored)

if __name__ == '__main__':
    arr_path = "../data/SCC.txt"
    graph = read_arr(arr_path)
    graph_rev = get_reversed_graph(graph)
    second = False
    DFS_loop(graph_rev)
    graph_new = get_new_graph(graph)
    graph_new_rev = get_reversed_graph(graph_new)
    second = True
    DFS_loop(graph_new)
    print(sorted([len(leader[k]) for k in leader.keys()], reverse=True)[:5])
