import matplotlib.pyplot as plt
import numpy as np
import math
import random


def unimodal_func(x):
    return math.cos(x) * math.tanh(x)


def multymodal_func(x):
    return unimodal_func(x) * math.sin(5 * x)


x_ = np.linspace(-2, 0, 100)
y1 = [unimodal_func(i) for i in x_]
y2 = [multymodal_func(i) for i in x_]


def show_graphic(name, x=None, y=None):
    fig = plt.figure(figsize=(7, 7))
    plt.plot(x, y)
    plt.title(name, fontsize=15)  # заголовок
    plt.xlabel("x", fontsize=14)  # ось абсцисс
    plt.ylabel("y", fontsize=14)  # ось ординат
    plt.grid(True)  # включение отображение сетки
    plt.show()
    fig.savefig(name)

show_graphic("Унимодальная функция", x_, y1)
show_graphic("Мультимодальная функция", x_, y2)


def is_transition(delta, t_i, iteration):
    if delta <= 0:
        iteration.append(1.)
        iteration.append(True)
        return True
    else:
        value = random.uniform(0, 1)
        p = math.exp(-delta / t_i)
        iteration.append(p)
        iteration.append(value <= p)
        return value <= p


def print_data(dataset):
    print(' N      T      x    f(x)      P     Transition')
    for i in dataset:
        print(f'{i[0]}  {i[1]:.3f}   {i[2]:.3f}   {i[3]:.3f}  {i[4]:.3f} {i[5]}')


def annealing(f, t_max, t_min, begin, end):
    t_cur = t_max
    all_iters = []
    counter = 1
    x = random.uniform(begin, end)
    while t_cur > t_min:
        one_iter = [counter, t_cur, x, f(x)]
        new_x = random.uniform(begin, end)
        delta = f(new_x) - f(x)
        if is_transition(delta, t_cur, one_iter):
            x = new_x
        counter += 1
        t_cur *= 0.95
        all_iters.append(one_iter)
    print(f'Result: x_min = {x:.3f} F_min = {f(x):.3f}')
    return all_iters


unimodal_results = annealing(unimodal_func, 10000, 0.01, -2, 0)
print_data(unimodal_results)
print('_________________________________________')
multymodal_results = annealing(multymodal_func, 10000, 0.01, -2, 0)
print_data(multymodal_results)

