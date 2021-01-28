import random as rd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def func(x):
    return -0.5 * x + 0


def error():
    return 2 * rd.uniform(-0.5, 0.5)


def noise(x_list):
    rd.seed(12)
    y_list = [func(x_i) + error() for x_i in x_list]
    return y_list


def get():
    x_list = np.linspace(-2, 2, 16)
    y_list = noise(x_list)
    return x_list, y_list


def show_noise_data(x_noise, y_noise):
    fig, ax = plt.subplots()
    ax.scatter(x_noise, y_noise)
    ax.set_title('Noise data')  # заголовок для Axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid()
    fig.set_figwidth(7)  # ширина и
    fig.set_figheight(7)  # высота "Figure"
    plt.savefig("images/Noise data.png")
    plt.show()


def mse(y_actual, y_pred):
    mse_error = 0
    for y, y_prime in zip(y_actual, y_pred):
        mse_error += (y - y_prime) ** 2
    return mse_error


def neuron(x_list, w1, w0):
    return [w1 * x + w0 for x in x_list]


def find_optimal_d(c_m, x_noise, y_noise):
    d_cur = rd.uniform(-1, 1)
    min_mse = mse(y_noise, neuron(x_noise, c_m, d_cur))
    d_min = d_cur
    for i in range(1, 1000):
        d_cur = rd.uniform(-1, 1)
        new_mse = mse(y_noise, neuron(x_noise, c_m, d_cur))
        if new_mse < min_mse:
            min_mse = new_mse
            d_min = d_cur
    return d_min


def find_optimal(x_noise, y_noise, data_=None):
    if data_ is None:
        data_ = []
    c_m = np.linspace(-1.5, 0.5, 1000)
    c_opt = c_m[0]
    d_opt = find_optimal_d(c_opt, x_noise, y_noise)
    min_mse = mse(y_noise, neuron(x_noise, c_opt, d_opt))
    data_.append([d_opt, c_opt, min_mse])
    for i in range(1, 1000):
        d_new = find_optimal_d(c_m[i], x_noise, y_noise)
        new_mse = mse(y_noise, neuron(x_noise, c_m[i], d_new))

        if new_mse < min_mse:
            d_opt = d_new
            c_opt = c_m[i]
            min_mse = new_mse
            data_.append([d_new, c_m[i], new_mse])
    return c_opt, d_opt, min_mse, data


def show_regression(x_noise, y_noise, c_opt, d_opt):
    fig, ax = plt.subplots()
    ax.scatter(x_noise, y_noise)
    ax.set_title('Found function')  # заголовок для Axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    fig.set_figwidth(7)  # ширина и
    fig.set_figheight(7)  # высота "Figure"
    ax.plot(x_noise, neuron(x_noise, c_opt, d_opt), color='red', linewidth=2)
    ax.grid()
    plt.legend(["regression", "data"])
    plt.savefig("images/Regression.png")
    plt.show()


if __name__ == '__main__':
    X, Y = get()
    show_noise_data(X, Y)
    data = []
    c, d, mse_min, data = find_optimal(X, Y, data)
    show_regression(X, Y, c, d)
    df = pd.DataFrame(data, columns=["w0", "w1", "error"])
    df.to_csv("results/data.csv")
    print(df)
    print("Optimal weights:")
    print(f"w0 = {d}")
    print(f"w1 = {c}")
    print(f"MSE = {mse_min}")
    print("Linear regression:")
    print(f"y = {c}x + {d}")
