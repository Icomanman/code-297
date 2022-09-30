
from sys import exit as exit_

from matrices import matrixMult, scalarMult  # NOQA
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
    B = 0
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

            j = [[dxs, dys], [dxt, dyt]]
            det = (dxs * dyt) - (dxt * dys)

            if det <= 0:
                exit_('Determinant Error.')

            jinv = 1
            B = B
    return B
