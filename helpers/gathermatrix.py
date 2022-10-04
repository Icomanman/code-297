

def gathermatrix(ke, el, kglob, elementtype='quad'):

    if elementtype == 'quad':
        K = [val for val in kglob]  # copy of kglob
        nodekeys = ['A', 'B', 'C', 'D']
        for node in range(len(nodekeys)):
            nodeno = el[f'node_{nodekeys[node]}']
            for x in range(2):
                for y in range(2):
                    K[nodeno + x][nodeno + y] = ke[node + x][node + y]

    elif elementtype == 'tri':
        K = 1
    return K
