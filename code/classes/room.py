# class met alle zalen en zaalgrootte

class Room(object):
    """

    """

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name}, {self.capacity}"
