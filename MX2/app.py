
import json
import os
import sys
import numpy as np

sys.path.append(f'{os.getcwd()}/helpers')

from modelparser import getmodel  # NOQA
from klocal import ke  # NOQA
from gathermatrix import gathermatrix  # NOQA
from Elements import ParentQuad  # NOQA


def main():
    sd = 2  # 2D - dimensional space
    modeldir = os.getcwd() + '/MX2/model'

    modelfile = '2d.json'
    srcfile = f'{modeldir}/src.json'

    model = getmodel(f'{modeldir}/{modelfile}', srcfile, True)

    nodes = model['nodes']
    elements = model['elements']
    nodecount = len(nodes.keys())
    elcount = len(elements.keys())

    coords = list()
    for node in nodes:
        coords.append(
            {'x': nodes[node]['x'], 'y': nodes[node]['y'], 'z': nodes[node]['z']})
        # z may be drop to save space (for this case - 2D only)

    # init the global matrix
    matsize = sd * nodecount
    K = np.zeros((matsize, matsize), float)

    for el in elements:
        quadelem = ParentQuad(elements[el], el, nodes)
        elemk = ke(quadelem, 2)
        K_ = gathermatrix(elemk, elements[el], K, 'quad')
        K = np.add(K, K_)

    out = open(f'{os.getcwd()}/K.csv', 'w')
    for lines in range(len(K[0])):
        for entry in range(len(K[0])):
            out.write(str(K[lines][entry]) + ',')
        out.write('\n')
    out.close()
    return K


if __name__ == '__main__':
    main()
