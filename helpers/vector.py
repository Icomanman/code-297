
def vecToFloat(filename=None, src=None):
    v = list()
    if(filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                v.append(float(line))
    return v
