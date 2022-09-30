
def dmatrix(E, v, type='plane_stress'):
    Emod = E / (1 - v**2)
    D = [
        [Emod,      Emod * v,   0],
        [Emod * v,  Emod,       0],
        [0,         0,          Emod * 0.5 * (1-v)]
    ]
    return D
