import numpy as np
import time

n_comps1 = 0
n_comps2 = 0
n_comps3 = 0

def partition1(arr, l, r):
    # 1. pivot is first element
    pivot = arr[l]
    i, j = l+1, l+1
    for j in range(l+1, r):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

def partition2(arr, l, r):
    # 2. pivot is last element
    pivot = arr[r-1]
    arr[l], arr[r-1] = arr[r-1], arr[l]
    i, j = l+1, l+1
    for j in range(l+1, r):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

def partition3(arr, l, r):
    # 3. pivot is median of three
    left, right = arr[l], arr[r-1]
    if (r-l) % 2 == 0:
        med_ind = (r+l)//2 - 1
    else:
        med_ind = (r+l)//2
    med = arr[med_ind]
    s = sorted([left, med, right])
    if s[1] == left:
        pivot = left
    elif s[1] == med:
        pivot = med
        arr[l], arr[med_ind] = arr[med_ind], arr[l]
    elif s[1] == right:
        pivot = right
        arr[l], arr[r-1] = arr[r-1], arr[l]
    i, j = l+1, l+1
    for j in range(l+1, r):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

def quicksort1(arr, l, r):
    if r <= l:
        return
    m = partition1(arr, l, r)
    global n_comps1
    n_comps1 += r-l-1
    quicksort1(arr, l, m)
    quicksort1(arr, m+1, r)

def quicksort2(arr, l, r):
    if r <= l:
        return
    m = partition2(arr, l, r)
    global n_comps2
    n_comps2 += r-l-1
    quicksort2(arr, l, m)
    quicksort2(arr, m+1, r)

def quicksort3(arr, l, r):
    if r <= l:
        return
    m = partition3(arr, l, r)
    global n_comps3
    n_comps3 += r-l-1
    quicksort3(arr, l, m)
    quicksort3(arr, m+1, r)

if __name__ == '__main__':
    tic = time.time()
    arr_path = r'../data/QuickSort.txt'
    arr = np.loadtxt(arr_path)
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    quicksort1(arr1, 0, len(arr1))
    quicksort2(arr2, 0, len(arr2))
    quicksort3(arr3, 0, len(arr3))
    print(f'#1 {n_comps1}\n#2 {n_comps2}\n#3 {n_comps3}')
    toc = time.time()
    print(toc-tic)
