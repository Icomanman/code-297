

class ParentQuad():
    # init to None (NoneType)
    x = [None, None, None, None]
    y = [None, None, None, None]

    def __init__(self, element, number, nodes):
        self.number = int(number)
        self.nodes = [element['node_A'], element['node_B'],
                      element['node_C'], element['node_D']]

        for i in range(len(self.x)):
            # nodes is a dict, hence the explicit casting, str
            self.x[i] = nodes[str(self.nodes[i])]['x']
            self.y[i] = nodes[str(self.nodes[i])]['y']
            # z is ommitted: 29 Sep 2022
