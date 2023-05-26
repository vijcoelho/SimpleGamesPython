class Ship:
    def __init__(self, name, size, qtd):
        self.name = str(name)
        self.size = size
        self.qtd = qtd

    def getQtd(self):
        return self.qtd
        