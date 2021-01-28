import matplotlib.pyplot as plt
import numpy as np
import math as m


def to_restrictions(weights, restrictions):
    """Возвращает индексы жизнеспособных альтернатив по
    порядку на основе главного критерия"""
    assert 1. in restrictions, "There is no main criteria"
    main = np.where(restrictions == 1.)
    assert len(main), "There could only be one main criteria"
    maxes = np.max(np.transpose(weights), axis=1)
    indicators = np.array([w >= restrictions * maxes for w in weights.astype(float)])
    indicators[:, main] = True
    return np.flatnonzero(np.all(indicators, axis=1))


def euclidean_metric(s_point, f_point):
    return m.sqrt((s_point[0] - f_point[0]) ** 2 + (s_point[1] - f_point[1]) ** 2)


def pareto_set(weights, criteria, utopia, cr_names, names):
    """Строит множество Парето, вычисляет расстояния
    и возвращает индекс наилучшего решения"""
    assert len(criteria) == 2, "There should only be 2 criteria"
    points = weights[:, criteria]
    dist = [euclidean_metric(point, utopia) for point in points]
    x, y = np.transpose(points)
    colors = np.random.rand(len(x))
    plt.title('Pareto set')
    plt.scatter(x, y, c=colors)
    for i, label in enumerate(names):
        plt.annotate(label, (x[i], y[i]))
    plt.scatter(*utopia, c='red')
    plt.annotate('U. point', utopia)
    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 11))
    if cr_names is None:
        names = ['x', 'y']
    plt.xlabel(cr_names[0])
    plt.ylabel(cr_names[1])
    plt.grid(linestyle='--')
    plt.savefig('pareto.png')
    return dist


def create_weights_matrix(amount, pairwise_comparisons, inv_function):
    """Создает матрицу весов"""
    result = [[1. for _ in range(amount)] for _ in range(amount)]
    offset = 0
    for i in range(amount - 1):
        j = amount - 1 - i
        straight = pairwise_comparisons[offset:offset + j]
        result[i][i + 1:] = straight
        mirrored = [inv_function(elem) for elem in straight[::-1]]
        result[j][:j] = mirrored
        offset += j
    return result


def normalized_priority_vector(matrix):
    """Нормализация строк матрицы"""
    geometric_means = np.array([np.prod(row) ** (1. / len(matrix)) for row in matrix])
    geometric_means_sum = np.sum(geometric_means)
    return geometric_means, geometric_means / geometric_means_sum


def consistency(matrix, npv, rci):
    """Вычисление коэффициента согласованности"""
    column_sums = np.sum(np.transpose(matrix), axis=1)
    own_value = sum(np.multiply(column_sums, npv))
    cons_i = (own_value - len(npv)) / (len(npv) - 1)
    return cons_i / rci