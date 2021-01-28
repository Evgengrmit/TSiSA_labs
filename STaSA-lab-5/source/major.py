import criteria as cr
import numpy as np

# Выбор дороги:
# А. Автострада;
# В. Шоссе;
# С. Грунтовка;
# D. Проселок

# Критерии
# 1. Расстояние;
# 2. Качество покрытия;
# 3. Контроль;
# 4. Инфраструктура.
if __name__ == '__main__':
    names = np.array(list('ABCD'))
    criteria_weights = np.array([2, 6, 8, 4])
    criteria_weights = np.divide(criteria_weights, np.sum(criteria_weights))
    criteria_matrix = np.array([[3, 9, 1, 8],
                                [5, 6, 3, 9],
                                [7, 4, 4, 4],
                                [9, 0, 1, 1]])
    lower_thresholds = np.array([0.4, 1, 0.6, 0.6])
    # lower_thresholds = np.array([0.4, 0.6, 0.3, 1])
    indices = cr.to_restrictions(criteria_matrix, lower_thresholds)

    # Report
    print('Метод главного критерия')
    print('Веса критериев:')
    print(np.round(criteria_weights, 2))
    print('Ограничения на веса:')
    print(lower_thresholds)
    print('Матрица критериев:')
    for i, row in zip(names, criteria_matrix):
        print(str(i), *row, sep=' | ')
    print('Альтернатива:')
    for i, row in zip(names[indices], criteria_matrix[indices]):
        print(str(i), *row, sep=' | ')
