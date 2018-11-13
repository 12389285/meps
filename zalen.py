# class met alle zalen en zaalgrootte

class Zalen(object):
    """
    Definieer de grootte van iedere zaal
    """

    def __init__(self, naam, capaciteit):
        self.naam = naam
        self.capaciteit = capaciteit

    def __str__(self):
        return f"{self.naam}: {self.capaciteit}"
        pass
