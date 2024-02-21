import numpy as np


def cal_Bellman(R, V_n, V_s, V_e, V_w):
    new_V = np.array([0, 1, 2, 3])

    for i in range(4):
        if i == 0:  # north
            new_V[0] = (
                0.7 * (R + V_n) + 0.1 * (R + V_s) + 0.1 * (R + V_e) + 0.1 * (R + V_w)
            )
        elif i == 1:  # south
            new_V[1] = (
                0.7 * (R + V_s) + 0.1 * (R + V_n) + 0.1 * (R + V_e) + 0.1 * (R + V_w)
            )
        elif i == 2:  # east
            new_V[2] = (
                0.7 * (R + V_e) + 0.1 * (R + V_n) + 0.1 * (R + V_s) + 0.1 * (R + V_w)
            )
        elif i == 3:  # west
            new_V[3] = (
                0.7 * (R + V_w) + 0.1 * (R + V_n) + 0.1 * (R + V_s) + 0.1 * (R + V_e)
            )
        else:  # error
            return 99999

    max_V = np.max(new_V)
    direction = np.where(max_V == new_V)

    return print("direction:", direction, "V=", max_V)
