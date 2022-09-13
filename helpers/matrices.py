import sys


def add(A, B):
    return


def matrix(m, n, src_file):
    if (m == None or n == None or src_file == None):
        sys.exit(1)

    A = list()
    with open(src_file, 'r') as f:
        for row in f.readlines():
            row_el = list()
            for el in row.strip():
                if(el != ' '):
                    row_el.append(float(el))
            A.append(row_el)

    print(f'A {m} x {n} matrix is created.')
    return A


def matrixMult(A, B):
    return


def scalarMult(A, B):
    return


def subtract(A, B):
    return


def trans(A):
    return


def vectorMult(A, B):
    return
