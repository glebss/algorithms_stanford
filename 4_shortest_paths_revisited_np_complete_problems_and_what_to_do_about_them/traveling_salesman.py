from numpy import sqrt
import itertools
import time
from tqdm import tqdm

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        n_cities = int(data[0].strip())
        coords = [tuple(map(float, d.strip().split())) for d in data[1:]]
    return coords, n_cities

INF = 1e6

if __name__ == "__main__":
    tic = time.time()
    arr_path = r'../data/tsp.txt'
    coords, n_cities = read_arr(arr_path)
    dists = {}
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            dists[(i+1, j+1)] = d
            dists[(j+1, i+1)] = d
    all_cities = [i+1 for i in range(n_cities)]
    A = {}
    A[((1,), 1)] = 0
    for m in range(2, n_cities+1):
        print(m)
        subsets = itertools.combinations(set(all_cities[1:]), m-1)
        subsets = [tuple([1] + list(s)) for s in subsets]
        for s in tqdm(subsets):
            if (s, 1) not in A:
                A[(s, 1)] = INF
            for j in s:
                if j == 1:
                    continue
                s_j = tuple([_ for _ in s if _ != j])
                A[(s, j)] = min([A[(s_j, k)] + dists[(k, j)] for k in s_j if k != j])
        keys_to_delete = [key for key in A.keys() if len(key[0]) <= m-1]
        for key in keys_to_delete:
            del A[key]
    ans = min([A[(tuple(all_cities), j)] + dists[(j, 1)] for j in all_cities[1:]])
    print(int(ans))
    toc = time.time()
    print(toc-tic)
