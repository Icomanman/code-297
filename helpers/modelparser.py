
import json
import os


def getmodel(filename, srcfile, savefile=False):
    model = dict()

    with open(srcfile) as f:
        modeldat = json.load(f)
        model['nodes'] = modeldat['nodes']
        model['elements'] = modeldat['meshed_plates']
        model['point_loads'] = modeldat['point_loads']

    if savefile:
        try:
            modelfile = open(filename, 'x')
        except:
            modelfile = open(filename, 'w')
        modelfile.write(json.dumps(model))
        modelfile.close()

    return model


def inpparser():
    # TODO
    model = 'TODO'
    return model


def mshparser():
    # TODO
    model = 'TODO'
    return model
