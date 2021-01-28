import criteria as cr
import numpy as np


if __name__ == '__main__':
    names = np.array(list('ABCD'))
    criteria_matrix = np.array([[3, 9, 1, 8],
                                [5, 6, 3, 9],
                                [7, 4, 4, 4],
                                [9, 0, 1, 1]])
    dist = cr.pareto_set(criteria_matrix, [0, 1], (10, 10), ['Distance','Road surface'], names)
    index = np.argmin(dist)
    # Report
    print('Матрица критериев:')
    for i, row in zip(names, criteria_matrix):
        print(i, *row, sep=' | ')
    print('Евклидово расстояние:')
    for i, d in zip(names, dist):
        print(i, d, sep=' | ')
    print('Альтернатива:')
    print(names[index], *criteria_matrix[index], sep=' | ')