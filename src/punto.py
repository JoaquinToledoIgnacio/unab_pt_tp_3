class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        "devuelve en representacion de string ambos valores"
        return f"({self.x}, {self.y})"

    def opuesto(self):
        "devuelve el punto opuesto"
        factor = -1
        return punto(-self.x * factor, -self.y * factor)

print("no se deberia ejecutar este codigo")
