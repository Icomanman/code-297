import os
import sys
sys.path.append(f'{os.getcwd()}/helpers')

from matrices import matrix, add, subtract, trans  # NOQA
from matrices import matrixMult, scalarMult, vectorMult  # NOQA
from vectors import vecToFloat  # NOQA

# hardcoded constants
A_file = './dat/A_Matrix24.dat'
b_file = './dat/b_vector24.dat'
test_dir = os.getcwd() + '/MX1/tests'


def main():
    print('This is an implementation of the Conjugate Gradient Method algorithm.')
    A = matrix(2, 2, test_dir + '/A.dat')
    b = vecToFloat(test_dir + '/b.dat')

    return


if __name__ == '__main__':
    main()
