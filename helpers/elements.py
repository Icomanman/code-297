

class ParentQuad():
    x = list()
    y = list()

    def __init__(self, element, number, *nodes):
        self.number = number
        self.nodes = [element['node_A'], element['node_B'],
                      element['node_C'], element['node_D']]
        # self.x = self.x.append(self.x1, self.x2, self.x3, self.x4)
        # self.y = self.y.append(self.y1, self.y2, self.y3, self.y4)
