import numpy as np

def calculate(l: list):
    if (len(l) != 9):
        raise ValueError("List must contain nine numbers.")
    m = [[l[0], l[1], l[2]],
        [l[3], l[4], l[5]],
        [l[6], l[7], l[8]]]

    mt = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        
    calculations = {
        "mean": [[np.mean(mt[0]), np.mean(mt[1]), np.mean(mt[2])], [np.mean(m[0]), np.mean(m[1]), np.mean(m[2])], np.mean(l)],
        "variance":[[np.var(mt[0]), np.var(mt[1]), np.var(mt[2])], [np.var(m[0]), np.var(m[1]), np.var(m[2])], np.var(l)],
        "standard deviation":[[np.std(mt[0]), np.std(mt[1]), np.std(mt[2])], [np.std(m[0]), np.std(m[1]), np.std(m[2])], np.std(l)],
        "max":[[np.max(mt[0]), np.max(mt[1]), np.max(mt[2])], [np.max(m[0]), np.max(m[1]), np.max(m[2])], np.max(l)],
        "min":[[np.min(mt[0]), np.min(mt[1]), np.min(mt[2])], [np.min(m[0]), np.min(m[1]), np.min(m[2])], np.min(l)],
        "sum":[[np.sum(mt[0]), np.sum(mt[1]), np.sum(mt[2])], [np.sum(m[0]), np.sum(m[1]), np.sum(m[2])], np.sum(l)],
    }

    return calculations