
import numpy as np


def solve(A, b, **params):

    A = A['val']
    print('This is an implementation of the Conjugate Gradient Method algorithm.')
    # param constants
    err = 0.001  # tolerance
    i_max = 100
    if 'err' in params:
        err = params['err']
    if 'i_max' in params:
        i_max = params['i_max']

    x = np.zeros(len(b))  # init solution vector

    # init
    i = 0
    Ax = np.matmul(A, x)
    r = np.subtract(b, Ax)
    d = r
    c_new = np.dot(r, r)
    c0 = c_new
    tol = c0 * (err ** 2)

    while i < i_max and c_new > tol:
        q = np.matmul(A, d)
        alpha = c_new / (np.dot(d, q))

        x = np.add(x, alpha * d)
        r = np.subtract(r, alpha * q)

        c_old = c_new
        c_new = np.dot(r, r)
        beta = c_new / c_old

        d = np.add(r, beta * d)
        i += 1

    return x
