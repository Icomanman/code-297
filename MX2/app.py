import numpy as np
from numpy import linalg as ln
import os
import sys

sys.path.append(f'{os.getcwd()}/helpers')

from matrices import matrix, trans  # NOQA
from k_loc import kLocal  # NOQA


def main():

    test_dir = os.getcwd() + '/MX1/tests'
    A = matrix(test_dir + '/A.dat')
    B = trans(A)
    print(B)
    C = np.array(A['val'])
    print(kLocal(A))
    return 0


if __name__ == '__main__':
    main()
