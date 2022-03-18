import numpy as np
import time

def sort_and_count(arr):
    if len(arr) == 1:
        return arr, 0
    if len(arr) == 2:
        if arr[1] < arr[0]:
            return arr[::-1], 1
        else:
            return arr, 0
    l = len(arr) // 2
    left_part, x = sort_and_count(arr[:l])
    right_part, y = sort_and_count(arr[l:])
    whole_arr = []
    z = 0
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            whole_arr.append(left_part[i])
            i += 1
        elif left_part[i] > right_part[j]:
            whole_arr.append(right_part[j])
            j += 1
            z += len(left_part) - i

    whole_arr.extend(left_part[i:])
    whole_arr.extend(right_part[j:])
    return whole_arr, x+y+z

def invs_brute_force(arr):
    n = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                n += 1
    return n


def main():

    arr_path = '../data/IntegerArray.txt'
    arr = np.loadtxt(arr_path)
    arr = list(arr)
    tic = time.time()
    _, n_invs = sort_and_count(arr)
    toc = time.time()
    t_fast = toc-tic
    print(f'fast algorithm time {t_fast}')
    tic = time.time()
    n_invs_bf = invs_brute_force(arr)
    toc = time.time()
    t_bf = toc-tic
    print(f'brute-force algorithm {t_bf}')
    print(f'ratio bf/fast {t_bf/t_fast:.2f}')

if __name__ == '__main__':
    main()
