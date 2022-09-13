
def vecToFloat(filename):
    v = list()
    with open(filename, 'r') as f:
        for line in f.readlines():
            v.append(float(line))

    return v
