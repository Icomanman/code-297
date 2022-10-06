
import os
import sys
import numpy as np

sys.path.append(f'{os.getcwd()}/helpers')

from modelparser import getmodel  # NOQA
from Elements import ParentQuad  # NOQA
from klocal import ke  # NOQA
from gathermatrix import gathermatrix  # NOQA
import conjugategradient  # NOQA


def loadvector(nodes, **loads):
    sd = loads['sd']

    # point loads
    pointloads = loads['p']
    nodalloads = dict(nodes)
    f = list([0] * sd * len(nodes))
    if sd == 2:
        for p in pointloads:
            nodalloads[p]['x'] = pointloads[p]['x_mag']
            nodalloads[p]['y'] = pointloads[p]['y_mag']
            nodeid = (pointloads[p]['node'] - 1) * 2
            f[nodeid] = pointloads[p]['x_mag']
            f[nodeid + 1] = pointloads[p]['y_mag']
    # TODO: traction loads
    return f


def writekcsv(K):
    out = open(f'{os.getcwd()}/tmp/K.csv', 'w')
    for lines in range(len(K[0])):
        for entry in range(len(K[0])):
            out.write(str(K[lines][entry]) + ',')
        out.write('\n')
    out.close()
    return 0


def main():
    sd = 2  # 2D - dimensional space
    modeldir = os.getcwd() + '/MX2/model'
    modelfile = '2d.json'
    srcfile = f'{modeldir}/src.json'

    # modeldir = os.getcwd() + '/MX2/test'
    # modelfile = 'test.json'
    # srcfile = f'{modeldir}/test_src.json'

    model = getmodel(f'{modeldir}/{modelfile}', srcfile, False)

    # model node and element numbers are assumed to be all SORTED
    # (translation from key-paired obj to arrays/list): 05 Oct 2022
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

    # writekcsv(elemk)
    f = loadvector(nodes, sd=sd, p=model['point_loads'])

    # determinant check
    Kdet = np.linalg.det(K)
    if Kdet == 0:
        sys.exit('> Determinant Error.')
    d = conjugategradient.solve(K, f)
    return d


if __name__ == '__main__':
    main()
