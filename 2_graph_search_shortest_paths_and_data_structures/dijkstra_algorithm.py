import time

def read_arr(arr_path):
    with open(arr_path, 'r') as f:
        data = f.readlines()
        data = [f.strip() for f in data]
        data = [el.split() for el in data]

    edges = []
    for el in data:
        source = int(el[0])
        for edge in el[1:]:
            dest, weight = list(map(int,edge.split(',')))
            edges.append((source, dest, weight))
    return edges

def Dijkstra(graph, s, n_vertices=200):
    X = {s}
    A, B = {}, {}
    A[s], B[s] = 0, []
    while len(X) != n_vertices:
        edges_needed = [e for e in graph if e[0] in X and e[1] not in X]
        min_edge = edges_needed[0]
        min_value = A[min_edge[0]] + min_edge[-1]
        for edge in edges_needed:
            value = A[edge[0]] + edge[-1]
            if value < min_value:
                min_value = value
                min_edge = edge
        X.add(min_edge[1])
        A[min_edge[1]] = min_value
        B[min_edge[1]] = B[min_edge[0]] + [min_edge[1]]
    return A, B

if __name__ == '__main__':
    tic = time.time()
    arr_path = "../data/dijkstraData.txt"
    edges = read_arr(arr_path)
    A, B = Dijkstra(edges, 1)
    toc = time.time()
    print(toc-tic)
