import matplotlib.pyplot as plt
import numpy as np
import math
import random
from decimal import *
from prettytable import PrettyTable


def unimodal_func(x_):
    return math.cos(x_) * math.tanh(x_)


def multymodal_func(x_):
    return unimodal_func(x_) * math.sin(5 * x_)


def get_table(data_massive):
    table = PrettyTable()
    field = ["q\\P"]
    field.extend(P)
    table.field_names = field
    for i in range(0, len(q)):
        row = [q[i]]
        row.extend(data_massive[i])
        table.add_row(row)
    return table


def getMin(func, n):
    random.seed(0)
    rand_x = random.uniform(-2, 0)
    y_min = func(rand_x)
    for i in range(1, n):
        rand_x = random.uniform(-2, 0)
        y_min = min(y_min, func(rand_x))
    return y_min


def get_results(func):
    results = []
    for i in range(0, len(q)):
        results.append([])
        for j in range(0, len(P)):
            n = number_of_points[i][j]
            results[i].append(round(Decimal(getMin(func, n)), 5))
    return results


x = np.linspace(-2, 0,100)
y1 = [unimodal_func(i) for i in x]
y2 = [multymodal_func(i) for i in x]


def show_graphic(name="", x_=None, y_=None):
    if y_ is None:
        y_ = []
    if x_ is None:
        x_ = []
    fig = plt.figure(figsize=(7, 7))
    plt.plot(x_, y_)
    plt.title(name, fontsize=15)  # заголовок
    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат
    plt.grid(True)  # включение отображение сетки
    plt.show()
    save = "Graphics/" + name + ".png"
    fig.savefig(save)


show_graphic("Унимодальная функция", x, y1)
show_graphic("Мультимодальная функция", x, y2)

P = np.arange(Decimal('0.9'), Decimal('1'), Decimal('0.01'))
q = np.arange(Decimal('0.005'), Decimal('0.105'), Decimal('0.005'))

number_of_points = []
for i in range(0, len(q)):
    number_of_points.append([])
    for j in range(0, len(P)):
        number_of_points[i].append(math.ceil(math.log(1 - P[j]) / math.log(1 - q[i])))
print("Зависимость N от P и q:")
print(get_table(number_of_points))

min_results_unimodal = get_results(unimodal_func)
print("Результаты поиска экстремума f(x) в зависимости от P и q:")
print(get_table(min_results_unimodal))
print("Результаты поиска экстремума f(x)*sin(5*x) в зависимости от P и q:")
min_results_multimodal = get_results(multymodal_func)
print(get_table(min_results_multimodal))
