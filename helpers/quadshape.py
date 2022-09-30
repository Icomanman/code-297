
# Shape Functions


def dels(t):
    # wrt s, partial derivatives of the shape functions
    c = 0.25
    dN1 = -c * (1 - t)
    dN2 = c * (1 - t)
    dN3 = c * (1 + t)
    dN4 = -c * (1 + t)
    dNs = [dN1, dN2, dN3, dN4]
    return dNs


def delt(s):
    # wrt t, partial derivatives of the shape functions
    c = 0.25
    dN1 = -c * (1 - s)
    dN2 = -c * (1 + s)
    dN3 = c * (1 + s)
    dN4 = c * (1 - s)
    dNt = [dN1, dN2, dN3, dN4]
    return dNt


def del_(physicalcoord, dN):
    # for dxs, dxt, dys and dyt - Jacobian elements
    d = 0
    for i in range(len(dN)):
        d = d + (physicalcoord[i] * dN[i])
    return d


def shape(s, t):
    # quad element shape functions (parent element)
    c = 0.25
    N1 = c * (1 - s) * (1 - t)
    N2 = c * (1 + s) * (1 - t)
    N3 = c * (1 + s) * (1 + t)
    N4 = c * (1 - s) * (1 + t)
    n = [N1, N2, N3, N4]
    N = [n, n]
    return N
