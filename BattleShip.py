class Ship:
    # def __init__(self, ship, destroyer, submarine, aircraft_carrier):
    #     self.ship = ship
    #     self.destroyer = destroyer
    #     self.submarine = submarine
    #     self.aircraft_carrier = aircraft_carrier
    
    def __init__(self, name, size, qtd):
        self.name = str(name)
        self.size = size
        self.qtd = qtd

    def getQtd(self):
        return self.qtd
        