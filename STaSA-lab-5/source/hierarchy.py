import criteria as cr
import numpy as np


def print_matrix(matrix, columns=None, form='.3f', sep=' | '):
    if columns is not None:
        print(*columns, sep=sep)
    for row in matrix:
        print(*[format(e, form) for e in row], sep=sep)


if __name__ == '__main__':
    # Random consistency criteria for 4x4 matrix
    rci = 0.90
    names = np.array(list('ABCD'))
    columns = ['A    ', 'B    ', 'C    ', 'D    ', 'GM   ', 'Norm ']

    print('Расстояние: ')
    criteria = [1 / 2, 1 / 3, 1, 1 / 3, 1 / 3, 1 / 2]
    criteria_weights = cr.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_1 = cr.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_1[:, np.newaxis]]),
                 columns)
    cons = cr.consistency(criteria_weights, npv_1, rci)
    print('Отношение согласованности: {}'.format(round(cons, 3)))

    print('Качество дорожного покрытия: ')
    criteria = [3, 7, 8, 4, 9, 5, 3]
    criteria_weights = cr.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_2 = cr.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_2[:, np.newaxis]]),
                 columns)
    cons = cr.consistency(criteria_weights, npv_2, rci)
    print('Отношение согласованности: {}'.format(round(cons, 3)))

    print('Контроль: ')
    criteria = [1 / 3, 1 / 5, 1 / 9, 1 / 3, 1 / 7, 1 / 5]
    criteria_weights = cr.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_3 = cr.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_3[:, np.newaxis]]),
                 columns)
    cons = cr.consistency(criteria_weights, npv_3, rci)
    print('Отношение согласованности: {}'.format(round(cons, 3)))

    print('Инфраструктура: ')
    criteria = [3, 5, 8, 4, 9, 3]
    criteria_weights = cr.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_4 = cr.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_4[:, np.newaxis]]),
                 columns)
    cons = cr.consistency(criteria_weights, npv_4, rci)
    print('Отношение согласованности: {}'.format(round(cons, 3)))

    print('Оценка приоритетов критериев: ')
    criteria = [2, 7, 9, 5, 3,2 ]
    criteria_weights = cr.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv = cr.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv[:, np.newaxis]]),
                 columns)
    cons = cr.consistency(criteria_weights, npv, rci)
    print('Отношение согласованности: {}'.format(round(cons, 3)))

    print('Нормальная матрица приоритетов:')
    npv_matrix = np.transpose([npv_1, npv_2, npv_3, npv_4])
    print_matrix(npv_matrix)
    print('Результирующий вектор')
    for i, j in zip(names, np.dot(npv_matrix, npv)):
        print(i, format(j, '.3f'), sep='|')
    print('Альтернатива:')
    print(names[np.dot(npv_matrix, npv).argmax()])