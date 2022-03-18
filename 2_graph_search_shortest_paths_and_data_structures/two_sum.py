import numpy as np
from tqdm import tqdm
import time


if __name__ == '__main__':
    tic = time.time()
    arr_path = r'../data/algo1-programming_prob-2sum.txt'
    arr = np.loadtxt(arr_path, dtype=int)
    arr = np.unique(arr)
    arr = sorted(arr)
    lower, higher = -1e4, 1e4
    sums = set()
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] > higher:
            j -= 1
        elif arr[i] + arr[j] < lower:
            i += 1
        else:
            for k in range(j, i-1, -1):
                s = arr[i] + arr[k]
                if s < lower:
                    break
                elif s >= lower and s <= higher and s not in sums:
                    sums.add(s)
            i += 1
    print(len(sums))
    toc = time.time()
    print(toc-tic)
