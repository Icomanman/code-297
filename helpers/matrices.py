import sys
import copy
# import csv
import re


def add(A, B):
    if (A['row'] != B['row'] and A['col'] != B['col']):
        print('> Err. size mismatch.')
        sys.exit(1)

    S = list()
    i = 0
    # row
    while i < A['row']:
        row_sum = list()
        j = 0
        # col
        while j < A['col']:
            row_sum.append(A['val'][i][j] + B['val'][i][j])
            j += 1
        # push
        S.append(row_sum)
        i += 1
    return S


def matrix(src_file):
    '''
    A_str = csv.reader(f)
        for row in A_str:
            row_el = list()
            for el in row:
                row_el.append(float(el))
            n = len(row)
            A.append(row_el)
        m = A_str.line_num
    '''
    A = list()
    with open(src_file, 'r') as f:
        A_str = f.readlines()
        m = len(A_str)  # row
        for row in A_str:
            # TODO: verify trailing whitespaces within the source file
            row_el = list()
            val = ''
            for el in row:
                if (bool(re.match('[0-9-.e]', el))):
                    val += el
                elif (val):
                    row_el.append(float(val))
                    # reset val
                    val = ''

            # append the last column
            if (val):
                row_el.append(float(val))

            n = len(row_el)  # col
            A.append(row_el)
    return {'val': A, 'row': m, 'col': n}


def matrixMult(A, B):
    # order: A x B
    if (A['row'] != B['col']):
        print('> Err. size mismatch.')
        sys.exit(1)

    S = list()
    for row_A in range(A['row']):
        row_el = list()
        for col_B in range(B['col']):
            el = 0.0  # init?
            for row_B in range(B['row']):
                el += A['val'][row_A][row_B] * B['val'][row_B][col_B]
            row_el.append(el)
        S.append(row_el)
    return S


def scalarMult(A, x):
    S = list()
    for row in A['val']:
        row_el = list()
        for el in row:
            row_el.append(float(el * x))
        S.append(row_el)
    return S


def subtract(A, B):
    # Order: A - B
    if (A['row'] != B['row'] and A['col'] != B['col']):
        print('> Err. size mismatch.')
        sys.exit(1)

    # de-reference the dict
    B = copy.deepcopy(B)
    i = 0
    # row
    while i < B['row']:
        j = 0
        # col
        while j < B['col']:
            B['val'][i][j] = -B['val'][i][j]
            j += 1
        # inc
        i += 1
    # invoke add
    S = add(A, B)
    return S


def trans(A):
    return


def vectorMult(A, b):
    if (A['row'] != len(b)):
        print('> Err. size mismatch.')
        sys.exit(1)

    S = list()
    for row in A['val']:
        row_el = 0.0  # init val?
        for i in range(len(row)):
            row_el += row[i] * b[i]
        S.append(row_el)
    return S
