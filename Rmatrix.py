import numpy as np
import random

def calc_combinations():
    allConfigs = []
    n = 1
    while len(allConfigs) < 16:
        config = []
        for i in range(4):
            config.append(random.choice([1,-1]))
        if config not in allConfigs:
            n += 1
            allConfigs.append(config)
    print(f"It took {n} iterations to get all combinations")
    return allConfigs

def check_R_condition(vec1, vec2):
    return (vec1[0] != vec2[0]) and (vec1[1] != vec2[1]) and (vec1[2] != vec2[2]) and vec1[3] != vec2[3]

def construct_R(matrix, configs):
    for i, row in enumerate(configs):
        for j, col in enumerate(configs):
            if check_R_condition(row, col):
                matrix[i][j] = 1
    return matrix

if __name__ == "__main__":
    combConfigs = calc_combinations()
    Rmatrix_empty = [[0 for x in range(16)] for y in range(16)]
    Rmatrix = construct_R(Rmatrix_empty, combConfigs)
    print(f"For the configurations \n{np.array(combConfigs)}")
    print(f'R = \n{np.array(Rmatrix)}')