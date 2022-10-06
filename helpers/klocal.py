
import sys
import numpy as np

from dmatrix import dmatrix  # NOQA
from quadshape import del_, dels, delt  # NOQA

# These constants could be moved as props of the ParentQuad class
E = 200000 * (10**6)
v = 0.3
Emod = E / (1 - v**2)
D = dmatrix(E, v)

params = {
    '2': {
        'c': [1.0, 1.0],
        'x': [-0.577350269, 0.577350269]
    },
    '3': {
        'c': [0.5555556, 0.8888889, 0.5555556],
        'x': [-0.77459669, 0.0, 0.77459669]
    },
    '4': {
        'c': [0.3478548, 0.6521452, 0.6521452, 0.3478548],
        'x': [-0.861136312, -0.339981044, 0.339981044, 0.861136312]
    }
}


def ke(el, gp):
    # assuming same Gauss points (gp) for both directions
    ke = np.zeros((8, 8))
    cn = params[str(gp)]['c']
    xn = params[str(gp)]['x']

    xcoords = el.x
    ycoords = el.y

    for i in range(gp):
        t = xn[i]

        for j in range(gp):
            s = xn[j]

            dNs = dels(t)
            dNt = delt(s)

            # Jacobian Elements
            dxs = del_(xcoords, dNs)
            dxt = del_(xcoords, dNt)
            dys = del_(ycoords, dNs)
            dyt = del_(ycoords, dNt)

            J = [[dxs, dys], [dxt, dyt]]
            det = (dxs * dyt) - (dxt * dys)

            if det <= 0:
                sys.exit('Determinant Error.')

            Jinv = [[dyt / det, -dys / det], [-dxt / det, dxs / det]]

            dN = np.matmul(Jinv, [dNs, dNt])
            dNx = dN[0]
            dNy = dN[1]

            B = np.zeros((3, 8))  # B size is specific to this problem
            for k in range(0, 2 * len(dNx), 2):
                B[0][k] = dNx[int(k / 2)]

            for l in range(0, 2 * len(dNy), 2):
                B[1][int(l + 1)] = dNy[int(l / 2)]

            B[2] = np.add(B[0], B[1])

            Btrans = np.transpose(B)
            k_ = cn[i] * cn[j] * np.matmul(Btrans, np.matmul(D, B)) * det
            ke = np.add(ke, k_)

    return ke
