import math
from tqdm import tqdm

def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        n_cities = int(data[0].strip())
        coords = [tuple(map(float, d.strip().split()))[1:] for d in data[1:]]
    return coords, n_cities

if __name__ == "__main__":
    arr_path = "../data/tsp_heur.txt"
    coords, n_cities = read_arr(arr_path)
    dists = {}
    coords = {i+1: coords[i] for i in range(len(coords))}
    n_visited = 1
    cur_city = 1
    not_visited = set([i+1 for i in range(len(coords))])
    not_visited.remove(1)
    d_overall = 0
    while n_visited < len(coords):
        # 1. find closest city to cur_city
        x1, y1 = coords[cur_city]
        d = 1e8
        min_city = cur_city
        for city in tqdm(not_visited):
            x2, y2 = coords[city]
            d_cur = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if d > d_cur:
                d = d_cur
                min_city = city
        cur_city = min_city
        not_visited.remove(cur_city)
        d_overall += d
        n_visited += 1

    x1, y1 = coords[1]
    x2, y2 = coords[cur_city]
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    d_overall += d
    print(int(d_overall))
