import numpy as np
from tqdm import tqdm
import time

def read_array(path):
    with open(path, 'r') as f:
        data = f.readlines()
    data = [el.strip() for el in data]
    arr = []
    for el in data:
        el = el.replace('\t', ' ').replace('\n', '')
        el = [int(i) for i in el.split(' ')]
        arr.append(el)
    return arr

def get_edges(vertices):
    edges = []
    for v_list in vertices:
        for v in v_list[1:]:
            edges.append(tuple(sorted((v_list[0], v))))
    edges = list(set(edges))
    return edges

def get_vertices_dict(vertices):
    return {v[0]: v[1:] for v in vertices}

def RContraction(vertices_dict):
    while len(vertices_dict.keys()) > 2:
        vert1 = np.random.choice(list(vertices_dict.keys()))
        vert2 = np.random.choice(vertices_dict[vert1]) # this will be deleted

        for vert in vertices_dict[vert2]:
            if vert == vert1:
                continue
            vertices_dict[vert1].append(vert)

        for vert in vertices_dict.keys():
            vertices_dict[vert] = [v if v != vert2 else vert1 for v in vertices_dict[vert]]
            if vert == vert1:
                vertices_dict[vert] = [v for v in vertices_dict[vert] if v != vert]

        del vertices_dict[vert2]

    k = np.random.choice(list(vertices_dict.keys()))
    return len(vertices_dict[k])

if __name__ == '__main__':
    tic = time.time()
    arr_path = r'../data/kargerMinCut.txt'
    vertices = read_array(arr_path)
    vertices_dict = get_vertices_dict(vertices)
    m = len(vertices) * (len(vertices) - 1) / 2
    n_trials = int(np.ceil(len(vertices) * np.log(len(vertices))))
    for _ in tqdm(range(n_trials)):
        min_cut = RContraction(get_vertices_dict(vertices))
        if m > min_cut:
            m = min_cut
    print(m)
    toc = time.time()
    print(toc-tic)
