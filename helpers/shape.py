
# Shape Functions

def delSQuad(t):
    c = 0.25
    N1 = -c * (1 - t)
    N2 = c * (1 - t)
    N3 = c * (1 + t)
    N4 = -c * (1 + t)
    n = [N1, N2, N3, N4]
    N = [n, n]
    return N


def delTQuad(s):
    c = 0.25
    N1 = -c * (1 - s)
    N2 = -c * (1 + s)
    N3 = c * (1 + s)
    N4 = c * (1 - s)
    n = [N1, N2, N3, N4]
    N = [n, n]
    return N


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
