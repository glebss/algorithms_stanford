from random import getrandbits, sample
import numpy as np
from tqdm import tqdm


def read_arr(path):
    with open(path, 'r') as f:
        data = f.readlines()
        n_vars = int(data[0].strip())
        vars = [None for _ in range(n_vars)]
        data = [tuple(map(int, d.strip().split())) for d in data[1:]]
        clauses = data
        vars_in_clauses = {}
        for d in tqdm(data):
            el1, el2 = d
            vars_in_clauses.setdefault(abs(el1), set())
            vars_in_clauses.setdefault(abs(el2), set())
            vars_in_clauses[abs(el1)].add(d)
            vars_in_clauses[abs(el2)].add(d)
            vars[abs(el1)-1] = bool(getrandbits(1))
            vars[abs(el2)-1] = bool(getrandbits(1))
        return clauses, vars_in_clauses, vars, n_vars

def check_clause(c):
    el1, el2 = c
    el1_bool = vars[abs(el1)-1]
    el2_bool = vars[abs(el2)-1]
    if el1 < 0 and el2 < 0:
        return not el1_bool or not el2_bool
    elif el1 < 0:
        return not el1_bool or el2_bool
    elif el2 < 0:
        return el1_bool or not el2_bool
    else:
        return el1_bool or el2_bool

if __name__ == "__main__":
    # preliminary answer
    # 101100
    arr_path = "../data/two_sat_2.txt"
    clauses, vars_in_clauses, vars, n_vars = read_arr(arr_path)
    possible = False
    for _ in range(10):
        if possible:
            break
        # random initial assignment
        vars = [bool(getrandbits(1)) for k in range(n_vars)]
        best_vars = vars.copy()
        n_true = len([c for c in clauses if check_clause(c)])
        best_n_true = n_true
        for j in tqdm(range(10)):
            vars = [bool(getrandbits(1)) for k in range(n_vars)]
            n_true = len([c for c in clauses if check_clause(c)])
            if n_true > best_n_true:
                best_n_true = n_true
                best_vars = vars.copy()
        vars = best_vars
        del best_vars
        false_clauses = set([c for c in clauses if not check_clause(c)])
        for i in tqdm(range(4*n_vars)):
            if i % 100 == 0:
                print(len(false_clauses))
                if len(false_clauses) <= 2:
                    print(false_clauses)
            if not false_clauses:
                print('yes')
                possible = True
                break

            # change var
            clause = sample(false_clauses, 1)[0]
            el_to_change = np.random.choice(clause)
            vars[abs(el_to_change)-1] = not vars[abs(el_to_change)-1]

            # add new clause to false clauses and delete true clauses
            for c in vars_in_clauses[abs(el_to_change)]:
                if not check_clause(c):
                    false_clauses.add(c)
                if c in false_clauses and check_clause(c):
                    false_clauses.remove(c)
