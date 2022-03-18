import numpy as np
import time

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        size = int(data[0].strip().split()[0])
        data = [tuple(map(int,d.strip().split())) for d in data[1:]]
        values = [v[0] for v in data]
        weights = [w[1] for w in data]
    return values, weights, size

if __name__ == "__main__":
    tic = time.time()
    arr_path = r'../data/knapsack1.txt'
    values, weights, size = read_arr(arr_path)
    A = np.zeros((len(values)+1, size+1), dtype=int)
    # for j in range(size+1):
    for i in range(1, len(values)+1):
        for j in range(size+1):
            if weights[i-1] > j:
                A[i, j] = A[i-1, j]
            else:
                A[i, j] = max(A[i-1, j], A[i-1, j-weights[i-1]] + values[i-1])

    print(A[-1, -1])
    toc = time.time()
    print(toc-tic)
