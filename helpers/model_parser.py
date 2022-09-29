
import json
import os


def getModel(filename, savefile=False):
    file_ = f'{os.getcwd()}/MX2/model/src.json'
    model = dict()

    with open(file_) as f:
        model_dat = json.load(f)
        model['nodes'] = model_dat['nodes']
        model['elements'] = model_dat['meshed_plates']

    if savefile:
        try:
            model_file = open(filename, 'x')
        except:
            model_file = open(filename, 'w')
        model_file.write(json.dumps(model))
        model_file.close()

    return model


def inp_parser():
    # TODO
    model = 'TODO'
    return model


def msh_parser():
    # TODO
    model = 'TODO'
    return model