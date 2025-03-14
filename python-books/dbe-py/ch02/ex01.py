class Shape:
    def __init__(self, name):
        self.name = name
    def perimeter(self):
        raise NotImplementedError("perimeter")
    def area(self):
        raise NotImplementedError("area")