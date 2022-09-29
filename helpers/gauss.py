
import numpy as np
from shape import delsquad,  deltquad, jacobian, quad  # NOQA

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


def quadrature(n):
    q = 0
    for fn in range(n):
        c = params[str(n)]['c']
        x = params[str(n)]['x']
        q = c[fn] * x[fn]
    return q
