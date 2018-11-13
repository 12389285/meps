
import csv
from zalen import Zalen


INPUT_VAKKEN = "vakken.csv"
INPUT_ZALEN = "zalen.csv"

def open_zalen(INPUT_ZALEN):
    """
    Openen van de informatie van alle zaken. Returns een dictionary.
    """
    # open zalen
    with open(INPUT_ZALEN) as zalen:
        zaal_reader = csv.DictReader(zalen)
        # lijst met alle zalen
        zalen = []
        for row in zaal_reader:
            nummer = row['Zaalnummber']
            aantal = row['Max. capaciteit']
            zaal = Zalen(nummer, aantal)
            zalen.append(zaal)

    return zalen

def open_vakken(INPUT_ZALEN):
    """
    Openen van de informatie van alle vakken.
    """

    # open Vakken
    with open(INPUT_VAKKEN) as vakken:
        vak_reader = csv.DictReader(vakken)
        # lijst met alle vakken
        vak_naam = []
        for row in vak_reader:
            vak = row['Vakken voor periode 4']
            vak_naam.append(vak)

    return vak_naam

def main(INPUT_ZALEN, INPUT_VAKKEN):
    """
    Main function to control other functions
    """
    zalen = open_zalen(INPUT_ZALEN)

    vak_naam = open_vakken(INPUT_VAKKEN)

    print(zalen)


if __name__ == "__main__":
    main(INPUT_ZALEN, INPUT_VAKKEN)
