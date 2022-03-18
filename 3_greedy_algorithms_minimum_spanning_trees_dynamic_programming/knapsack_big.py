from knapsack import read_arr
import sys, resource
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))
import time


def recursive_knapsack(n_items, capacity):
    if (n_items, capacity) in seen_so_far:
        return seen_so_far[(n_items, capacity)]

    if n_items == 1:
        if capacity >= weights[0]:
            return values[0]
        else:
            return 0

    value, weight = values[n_items-1], weights[n_items-1]
    if weight <= capacity:
        left = recursive_knapsack(n_items-1, capacity)
        took = recursive_knapsack(n_items-1, capacity-weight) + value
        seen_so_far[(n_items-1, capacity)] = left
        seen_so_far[(n_items, capacity)] = max(left, took)
        return max(left, took)
    else:
        left = recursive_knapsack(n_items-1, capacity)
        seen_so_far[(n_items-1, capacity)] = left
        seen_so_far[(n_items, capacity)] = left
        return left

if __name__ == "__main__":
    tic = time.time()
    arr_path = r"../data/knapsack_big.txt"
    values, weights, size = read_arr(arr_path)
    seen_so_far = {}
    print(recursive_knapsack(len(values), size))
    toc = time.time()
    print(toc-tic)
