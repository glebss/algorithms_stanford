import time

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        data = [d.strip() for d in data]
        n_vert, n_edge = tuple(map(int, data[0].split()))
        edges = [tuple(map(int, d.split())) for d in data[1:]]
    return edges, n_vert, n_edge

def prims_algorithm(edges, n_vert=500):
    mst = []
    X = set()
    X.add(edges[0][0])
    while len(X) != n_vert:
        edges_needed = [e for e in edges if (e[0] in X and e[1] not in X) or (e[1] in X and e[0] not in X)]
        min_cost = edges_needed[0][-1]
        min_edge = edges_needed[0]
        for edge in edges_needed:
            if edge[-1] < min_cost:
                min_cost = edge[-1]
                min_edge = edge
        mst.append(min_edge)
        X.add(min_edge[0])
        X.add(min_edge[1])

    costs = [e[-1] for e in mst]
    return sum(costs)

if __name__ == "__main__":
    tic = time.time()
    arr_path = "../data/edges.txt"
    edges, n_vert, n_edge = read_arr(arr_path)
    costs = prims_algorithm(edges, n_vert=n_vert)
    print(costs)
    toc = time.time()
    print(toc-tic)
