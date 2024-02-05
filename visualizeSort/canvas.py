from abc import ABC

class Canvas(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.canvas = None


