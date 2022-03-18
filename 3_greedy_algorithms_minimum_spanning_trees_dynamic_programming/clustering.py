import time

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        data = [d.strip() for d in data]
        n_nodes = int(data[0])
        data = [list(map(int, d.split())) for d in data[1:]]
    edges = [d for d in data]
    return edges, n_nodes


if __name__ == "__main__":
    tic = time.time()
    arr_path = "../data/clustering1.txt"
    edges, n_nodes = read_arr(arr_path)
    clusters = {}
    for e in edges:
        if not clusters.get(e[0]):
            clusters[e[0]] = e[0]
        if not clusters.get(e[1]):
            clusters[e[1]] = e[1]

    edges = sorted(edges, key=lambda x: x[-1], reverse=True)
    num_clusters = len(set(clusters.values()))
    while num_clusters > 4:
        min_edge = edges.pop()
        node_1, node_2 = min_edge[:2]
        cluster_1, cluster_2 = clusters[node_1], clusters[node_2]
        if cluster_1 == cluster_2:
            continue
        # change clusters
        for key, value in clusters.items():
            if value == cluster_2:
                clusters[key] = cluster_1
        num_clusters -= 1
    min_edge = edges.pop()
    node_1, node_2 = min_edge[:2]
    cluster_1, cluster_2 = clusters[node_1], clusters[node_2]
    d = min_edge[-1]
    while cluster_1 == cluster_2:
        min_edge = edges.pop()
        node_1, node_2 = min_edge[:2]
        cluster_1, cluster_2 = clusters[node_1], clusters[node_2]
        d = min_edge[-1]
    print(d)
    toc = time.time()
    print(toc-tic)
