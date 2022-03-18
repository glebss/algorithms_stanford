import numpy as np
from tqdm import tqdm
import time

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
    n_vert, n_edges = tuple(map(int, data[0].strip().split()))
    edges = [tuple(map(int, d.strip().split())) for d in data[1:]]
    edges = {e[:2] : e[-1] for e in edges}
    return edges, n_vert, n_edges

INF = int(1e6)

if __name__ == "__main__":
    tic = time.time()
    arr_path1 = "../data/g1.txt"
    arr_path2 = "../data/g2.txt"
    arr_path3 = "../data/g3.txt"

    ans = 1e6
    for arr_path in [arr_path1, arr_path2, arr_path3]:
        print(arr_path)
        edges, n_vert, n_edges = read_arr(arr_path)
        A = np.zeros((n_vert, n_vert, n_vert), dtype='int64')

        # base case
        for i in tqdm(range(n_vert)):
            for j in range(n_vert):
                if i == j:
                    A[i, j, 0] = 0
                elif (i+1, j+1) in edges:
                    A[i, j, 0] = edges[(i+1, j+1)]
                else:
                    A[i, j, 0] = INF

        for k in tqdm(range(1, n_vert, 1)):
            for i in range(n_vert):
                for j in range(n_vert):
                    A[i, j, k] = min(A[i, j, k-1], A[i, k, k-1] + A[k, j, k-1])

        # check for negative cycle
        has_negative_cycle = False
        for i in range(n_vert):
            if A[i, i, -1] < 0:
                has_negative_cycle = True
                break
        if not has_negative_cycle:
            if np.min(A) < ans:
                ans = np.min(A)
        del A
    print(ans)
    toc = time.time()
    print(toc-tic)
