# class met alle zalen en zaalgrootte

class zalen()
    ""Definieer de grootte van iedere zaal"

    def __init__(self, naam, grootte):
        self.naam = naam
        self.grootte = zaalgrootte

    def __str__(self):
        return f"{self.naam}: {self.grootte}"
        pass
