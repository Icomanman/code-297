
import os
import sys
import numpy as np
from numpy import linalg as ln

sys.path.append(f'{os.getcwd()}/helpers')

from model_parser import getModel  # NOQA
from matrices import matrix, trans  # NOQA
from k_loc import kLocal  # NOQA


def main():
    model_dir = os.getcwd() + '/MX2/model'
    model = getModel(f'{model_dir}/2d.json')

    return 0


if __name__ == '__main__':
    main()
