
import json
import os


def getmodel(filename, savefile=False):
    # file_ = f'{os.getcwd()}/MX2/model/src.json'
    file_ = f'{os.getcwd()}/MX2/model/iso_src.json'
    model = dict()

    with open(file_) as f:
        modeldat = json.load(f)
        model['nodes'] = modeldat['nodes']
        model['elements'] = modeldat['meshed_plates']

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
