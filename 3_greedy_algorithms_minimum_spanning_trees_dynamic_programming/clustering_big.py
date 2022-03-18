import sys, resource
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))
import time
from tqdm import tqdm

def read_arr(arr_path):
    with open(arr_path, 'r') as f:
        data = f.readlines()
        data = [d.strip().replace(' ', '') for d in data[1:]]
        
    return data

def hamming_distance(str1, str2):
    assert len(str1) == len(str2)
    dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dist += 1
    return dist

def get_all_one_bit_perms(node):
    perms = []
    for i in range(len(node)):
        s = node[i]
        new_node = node[:i] + str(int(not int(s))) + node[i+1:]
        perms.append(new_node)
    return perms

def get_all_two_bit_perms(node):
    perms = []
    for i in range(len(node)):
        for j in range(i+1, len(node)):
            s1, s2 = node[i], node[j]
            new_node = node[:i] + str(int(not int(s1))) + \
                       node[i+1:j] + str(int(not int(s2))) + \
                       node[j+1:]
            perms.append(new_node)
    return perms

def update_neighbors(node, clusters, curr_cluster):
    clusters[node] = curr_cluster
    perms = get_all_one_bit_perms(node) + get_all_two_bit_perms(node)
    perms_needed = []
    for p in perms:
        if clusters.get(p):        
            perms_needed.append(p)
    if not perms_needed:
        return
    for p in perms_needed:
        if clusters[p] == -1:
            update_neighbors(p, clusters, curr_cluster)


if __name__ == '__main__':
    tic = time.time()
    arr_path = "data/clustering_big.txt"
    nodes = read_arr(arr_path)
    nodes = list(set(nodes))
    clusters = {n: -1 for n in nodes}
    curr_cluster = 0
    for node in nodes:
        if clusters[node] != -1:
            continue
        update_neighbors(node, clusters, curr_cluster)
        curr_cluster += 1
    
    # for node in tqdm(nodes):
    #     if clusters[node] != -1:
    #         continue
    #     clusters[node] = curr_cluster
    #     neighbours = get_all_one_bit_perms(node) + get_all_two_bit_perms(node)
    #     for n in neighbours:
    #         clusters[n] = curr_cluster
    #     curr_cluster += 1
    print(len(set(clusters.values())))
    toc = time.time()
    print(toc-tic)
