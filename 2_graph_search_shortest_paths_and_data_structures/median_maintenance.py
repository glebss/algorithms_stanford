import numpy as np
from tqdm import tqdm
from heapq import heapify, heappop, heappush
import time


if __name__ == '__main__':
    tic = time.time()
    arr_path = '../data/Median.txt'
    arr = np.loadtxt(arr_path, dtype=int)
    heap_low, heap_high = [-min(arr[:2])], [max(arr[:2])]
    heapify(heap_low)
    heapify(heap_high)
    medians = [arr[0], -heap_low[0]]
    for el in tqdm(arr[2:]):
        # decide on which heap to push
        if el < heap_high[0]:
            heappush(heap_low, -el)
        else:
            heappush(heap_high, el)

        # balance heaps
        if len(heap_low) - len(heap_high) >= 2:
            heappush(heap_high, -heappop(heap_low))
        elif len(heap_high) - len(heap_low) >= 2:
            heappush(heap_low, -heappop(heap_high))

        assert abs(len(heap_low) - len(heap_high)) <= 1

        # extract median
        if len(heap_low) >= len(heap_high):
            medians.append(-heap_low[0])
        else:
            medians.append(heap_high[0])

    print(sum(medians) % 10000)
    toc = time.time()
    print(toc-tic)
