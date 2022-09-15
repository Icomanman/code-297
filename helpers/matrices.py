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
            row_el = list()
            val = ''
            for el in row:
                if (bool(re.match('[0-9-.]', el))):
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
    return


def scalarMult(A, B):
    return


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


def vectorMult(A, B):
    return
