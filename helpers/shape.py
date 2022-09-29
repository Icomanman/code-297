
# Shape Functions

def delsquad(t):
    c = 0.25
    dN1 = -c * (1 - t)
    dN2 = c * (1 - t)
    dN3 = c * (1 + t)
    dN4 = -c * (1 + t)
    dN = [dN1, 0, dN2, 0, dN3, 0, dN4, 0]
    return dN


def deltquad(s):
    c = 0.25
    dN1 = -c * (1 - s)
    dN2 = -c * (1 + s)
    dN3 = c * (1 + s)
    dN4 = c * (1 - s)
    dN = [0, dN1, 0, dN2, 0, dN3, 0, dN4]
    return dN


def quad(s, t):
    c = 0.25
    N1 = c * (1 - s) * (1 - t)
    N2 = c * (1 + s) * (1 - t)
    N3 = c * (1 + s) * (1 + t)
    N4 = c * (1 - s) * (1 + t)
    n = [N1, N2, N3, N4]
    N = [n, n]
    return N


def tri():
    N = 0
    return N
