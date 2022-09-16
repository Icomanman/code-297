
def vecToFloat(filename=None, src=None):
    v = list()
    if (filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                v.append(float(line))
    return v


def printVector(b):
    import os
    f = open(os.getcwd() + '/vector.out', 'w')
    for el in b:
        f.write(str(el) + '\n')
    f.close()
    return
