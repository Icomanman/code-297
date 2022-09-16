import sys

'''
All vectors are converted to a python list; source file must be 'neatly' written in a column
i.e., no trailing whitespaces
'''


def vector(size, init=0):
    if (size < 1):
        print('> vector: please input proper size.')
        sys.exit(1)
    elif (size > 1000):
        print('> vector: max size is 999.')
        sys.exit(1)
    v = list()
    i = 0
    while i < size:
        v.append(init)
        i += 1
    return v


def vectorAdd(a, b):
    v = list()
    for row in range(len(a)):
        v.append(float(a[row] + b[row]))
    return v


def vectorMult(a, b):
    v = 0
    i = 0
    while i < len(a):
        v += (float(a[i] * b[i]))
        i += 1

    return v


def vectorScalarMult(a, z):
    v = list()
    i = 0
    while i < len(a):
        v.append(float(a[i] * z))
        i += 1
    return v


def vectorSub(a, b):
    v = list()
    for row in range(len(a)):
        v.append(float(a[row] - b[row]))
    return v


def vecToFloat(filename=None, src=None):
    v = list()
    if (filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                v.append(float(line))
    return v


def vectorTrans(a):
    v = list()
    return v


def printVector(b):
    import os
    f = open(os.getcwd() + '/vector.out', 'w')
    for el in b:
        f.write(str(el) + '\n')
    f.close()
    return
