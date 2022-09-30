
from enum import Flag
import os
import sys
import numpy as np
from numpy import linalg as ln

sys.path.append(f'{os.getcwd()}/helpers')

from modelparser import getmodel  # NOQA
from klocal import ke  # NOQA
from Elements import ParentQuad  # NOQA


def gathermatrix(nodes, elementtype='quad'):
    nodelist = list(nodes.keys())

    if elementtype == 'quad':
        L = 1
    elif elementtype == 'tri':
        L = 1
    return L


def main():
    sd = 2  # 2D - dimensional space
    modeldir = os.getcwd() + '/MX2/model'
    # model = getmodel(f'{modeldir}/2d.json', True)
    model = getmodel(f'{modeldir}/iso.json', False)

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
    kglob = np.zeros((matsize, matsize), float)

    for el in elements:
        quadelem = ParentQuad(elements[el], el, nodes)
        elemk = ke(quadelem, 2)
        print(np.dot(elemk, 0.001))
        # kglob = np.add(kglob, elemk)

    return 0


if __name__ == '__main__':
    main()
