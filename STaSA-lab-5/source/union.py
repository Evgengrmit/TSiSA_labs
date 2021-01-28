import criteria as cr
import numpy as np

if __name__ == '__main__':
    names = np.array(list('ABCD'))
    comparisons = [0, 1, 0, 0, 0.5, 0]
    criteria_matrix = np.array([[3, 9, 1, 8],
                                [5, 6, 3, 9],
                                [7, 4, 4, 4],
                                [9, 0, 1, 1]])
    # Нормализация матрицы
    sums = np.sum(np.transpose(criteria_matrix), axis=1)
    criteria_matrix = np.divide(criteria_matrix, sums)

    # Создание массива весов из попарных сравнений
    weights = cr.create_weights_matrix(4, comparisons, lambda x: 1 - x)
    weights = np.sum(weights, axis=1)
    weights = weights / np.sum(weights)
    result = np.dot(criteria_matrix, weights)

    # Report
    print('Нормализированный вектор весов:')
    print(weights)
    print('Нормализированная матрица критериев:')
    for i, row in zip(names, criteria_matrix):
        print(i, *[format(e, '.3f') for e in row], sep=' | ')
    print('Объединенные критерии:')
    for i, r in zip(names, result):
        print(i, format(r, '.3f'), sep=' | ')
    print('Альтернатива:')
    print(names[result.argmax()])
