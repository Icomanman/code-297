import numpy as np
from numpy import linalg as matrix

from shape import delsquad,  deltquad, jacobian, quad  # NOQA


def ke(el):
    B = list()
    dNx = list()
    dNy = list()

    for y in el.y:
        dNx.append(delsquad(y))

    B.append(delsquad(el.y))
    B.append(deltquad(el.x))
    B.append(np.add(B[0], B[1]))
    k = 0
    return k
