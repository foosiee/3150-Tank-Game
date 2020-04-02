class GridNode:
    def __init__(self, coords, weight=1):
        self.coords = coords
        self.weight = weight
        self.is_empty = True

    def set_weight(self, weight):
        self.weight = weight

    def set_is_empty(self, is_empty):
        self.is_empty = is_empty