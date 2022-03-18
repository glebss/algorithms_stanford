import time

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        data = [int(d.strip()) for d in data[1:]]
    return data

if __name__ == '__main__':
    tic = time.time()
    arr_path = "../data/mwis.txt"
    data = read_arr(arr_path)
    data = [0] + data
    A = [0 for _ in data]
    A[1] = data[1]
    for i in range(2, len(data)):
        A[i] = max(A[i-2] + data[i], A[i-1])

    path = set()
    i = len(A) - 1
    while i > 0:
        if A[i-1] >= A[i-2] + data[i]:
            i -= 1
        else:
            path.add(i)
            i -= 2
    for i in [1, 2, 3, 4, 17, 117, 517, 997]:
        print(int(i in path), end='')
    toc = time.time()
    print()
    print(toc-tic)
