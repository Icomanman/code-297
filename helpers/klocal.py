import numpy as np

from bmatrix import bmatrix  # NOQA


def ke(el):
    B = bmatrix(el, 2)
    Btrans = np.transpose(B)
    k = 1
    return k
