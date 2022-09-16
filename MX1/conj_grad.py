import os
import sys
sys.path.append(f'{os.getcwd()}/helpers')

from matrices import matrix, add, subtract, trans  # NOQA
from matrices import matrixMult, scalarMult, vectorMMult  # NOQA
from vectors import vector, vecToFloat, printVector, vectorScalarMult  # NOQA
from vectors import vectorAdd, vectorMult, vectorSub  # NOQA

# hardcoded constants
dat_dir = os.getcwd() + '/MX1/dat'
test_dir = os.getcwd() + '/MX1/tests'
A_file = '/A_Matrix24.dat'
b_file = '/b_vector24.dat'


def conjGrad(A, b, checked=False):
    if (checked):
        B = dict()
        B['val'] = A
        B['row'] = A['row']
        B['col'] = A['col']
        A = dict(B)
    elif (A['row'] != len(b)):
        print('> Err. size mismatch.')
        sys.exit(1)

    print('This is an implementation of the Conjugate Gradient Method algorithm.')
    # param constants
    err = 0.001  # tolerance
    x = vector(len(b), 1)  # init solution vector

    i = 0
    i_max = 100
    # init
    Ax = vectorMMult(A, x)
    r = vectorSub(b, Ax)
    d = r
    c_new = vectorMult(r, r)
    c0 = c_new
    while i < i_max or c_new > (c0*(err ** 2)):
        q = vectorMMult(A, d)
        alpha = c_new / (vectorMult(d, q))

        x = vectorAdd(x, (vectorScalarMult(d, alpha)))
        r = vectorSub(r, vectorScalarMult(q, alpha))

        c_old = c_new
        c_new = vectorMult(r, r)
        beta = c_new / c_old

        d = vectorAdd(r, vectorScalarMult(d, beta))
        i += 1

    return x


def main():
    # A = matrix(test_dir + '/A.dat')
    # A = matrix(test_dir + '/B.dat')
    # A = matrix(test_dir + '/ones.dat')
    # b = vecToFloat(test_dir + '/b.dat')
    b = vecToFloat(test_dir + '/y.dat')

    A = matrix(dat_dir + A_file)
    # b = vecToFloat(dat_dir + b_file)

    # print(A['val'])
    # print(b)

    # print(add(A, A))
    # print(subtract(A, A))
    # print(scalarMult(A, 2))
    # print(vectorMult(A, b))
    # print(matrixMult(A, A))
    # print(trans(A))
    # print(matrixMult(A, trans(A), True))

    # print(f"size: {A['row']} x {A['col']}")
    x = conjGrad(A, b)
    print(x)
    return


if __name__ == '__main__':
    main()
