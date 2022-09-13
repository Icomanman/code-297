import sys
from vectors import vecToFloat


def dotProduct(v, u):
    if (len(v) < 1 or len(u) < 1):
        print('> Usage: v and u must be vectors.')
        return 1
    elif (len(v) != len(u)):
        print('> v and u must be of the same dimension.')
        sys.exit(1)

    i = 0
    dot_prod = 0  # setting default to 0 may cause issues later on

    while i < len(v):
        dot_prod += v[i] * u[i]
        i += 1

    print(f'The resulting dot product is {dot_prod}.')
    return dot_prod


if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print('Usage: dot_prod.py FILENAME.dat(vector 1) FILENAME.dat(vector 2')
        sys.exit(1)

    v = vecToFloat(sys.argv[1])
    u = vecToFloat(sys.argv[2])

    dotProduct(v, u)
