import numpy as np


def update_w(w, x, y_star):
    sum = np.sum(w * x)
    if sum >= 0:
        y = +1
    else:
        y = -1
    if y != y_star:
        w = w + y_star * x
    print("sum:", sum)
    return w


# サンプル1（AND関数）
x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y_star = np.array([-1, -1, -1, 1])
w = np.zeros(3)
for i in range(25):
    j = i % 4
    w = update_w(w, x[j, :], y_star[j])
    print(i + 1, w)

# サンプル2（XOR関数）
x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y_star = np.array([-1, 1, 1, -1])
w = np.zeros(3)
for i in range(12):
    j = i % 4
    w = update_w(w, x[j, :], y_star[j])
    print(i + 1, w)

# サンプル2（XOR関数） #実験
x = np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1], [1, 1, 1]])
y_star = np.array([1, 1, -1, -1])
w = np.array(3)
w = [-1, 0, -1]
for i in range(25):
    j = i % 4
    w = update_w(w, x[j, :], y_star[j])
    print(i + 1, w)
