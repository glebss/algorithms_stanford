import numpy as np
import time

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        data = [d.strip() for d in data[1:]]
        data = [tuple(map(int, d.split())) for d in data]
    return data

def calc_comp_time(jobs):
    times = np.cumsum([j[1] for j in jobs])
    weights = np.array([j[0] for j in jobs])
    return np.sum(times*weights, dtype=int)


if __name__ == '__main__':
    tic = time.time()
    arr_path = '../data/jobs.txt'
    jobs = read_arr(arr_path)
    jobs = sorted(jobs, key=lambda el: el[0]/el[1], reverse=True)
    comp_time = calc_comp_time(jobs)
    print(comp_time)
    toc = time.time()
    print(toc-tic)
