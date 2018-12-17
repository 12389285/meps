class Room(object):
    """
    This class classifies all the rooms.
    """

    def __init__(self, name, capacity):
        """
        The rooms have a name and a maximum capicity for students.
        """
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name}, {self.capacity}"
