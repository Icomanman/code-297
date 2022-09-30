
from sys import exit as exit_
import numpy as np
from quadshape import del_, dels, delt  # NOQA

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


def bmatrix(el, n):
    B = np.zeros((3, 8), float)
    cn = params[str(n)]['c']
    xn = params[str(n)]['x']

    xcoords = el.x
    ycoords = el.y

    for i in range(n):
        t = xn[i]

        for j in range(n):
            s = xn[j]

            dNs = dels(s)
            dNt = delt(t)

            # Jacobian Elements
            dxs = del_(xcoords, dNs)
            dxt = del_(xcoords, dNt)
            dys = del_(ycoords, dNs)
            dyt = del_(ycoords, dNt)

            J = [[dxs, dys], [dxt, dyt]]
            det = (dxs * dyt) - (dxt * dys)

            if det <= 0:
                exit_('Determinant Error.')

            Jinv = [[dyt/det, -dys/det], [-dxt/det, dxs/det]]

            dN = np.matmul(Jinv, [dNs, dNt])
            dNx = dN[0]
            dNy = dN[1]

            _ = np.zeros((3, 8))
            for k in range(0, 2*len(dNx), 2):
                _[0][k] = dNx[int(k/2)]

            for l in range(0, 2*len(dNy), 2):
                _[1][int(l+1)] = dNy[int(l/2)]

            _[2] = np.add(_[0], _[1])

            B = cn[j] * np.add(B, _)

        B = cn[i] * B
    return B
