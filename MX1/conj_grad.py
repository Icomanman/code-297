import os
import sys
sys.path.append(f'{os.getcwd()}/helpers')

from matrices import matrix, add, subtract, trans  # NOQA
from matrices import matrixMult, scalarMult, vectorMult  # NOQA
from vectors import vecToFloat  # NOQA

# hardcoded constants
dat_dir = os.getcwd() + '/MX1/dat'
test_dir = os.getcwd() + '/MX1/tests'
A_file = '/A_Matrix24.dat'
b_file = '/b_vector24.dat'


def main():
    print('This is an implementation of the Conjugate Gradient Method algorithm.')
    # A = matrix(test_dir + '/A.dat')
    A = matrix(dat_dir + A_file)
    # A = matrix(test_dir + '/ones.dat')
    # b = vecToFloat(test_dir + '/b.dat')
    # print(A['val'])
    # print(b)

    # print(subtract(A, A))
    # print(scalarMult(A, 2))
    # print(vectorMult(A, b))
    print(matrixMult(A, A))

    # print(f"size: {A['row']} x {A['col']}")
    return


if __name__ == '__main__':
    main()
