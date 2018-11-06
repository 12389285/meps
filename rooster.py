
import csv


INPUT_VAKKEN = "vakken.csv"
INPUT_ZALEN = "zalen.csv"

def files(INPUT_ZALEN, INPUT_VAKKEN):

    # open zalen
    with open(INPUT_ZALEN) as zalen:

        zaal_reader = csv.DictReader(zalen)

        zaal_nummers = []

        for row in zaal_reader:
            nummer = row['Zaalnummber']
            zaal_nummers.append(nummer)
        print(zaal_nummers)


    # open Vakken
    with open(INPUT_VAKKEN) as vakken:

        vak_reader = csv.DictReader(vakken)

        vak_namen = []
        for row in vak_reader:
            vak = row['Vakken voor periode 4']
            vak_namen.append(vak)
        print(vak_namen)

if __name__ == "__main__":
    files(INPUT_ZALEN, INPUT_VAKKEN)
