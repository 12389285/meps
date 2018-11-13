
import csv
from room import Room
from vakken import Vakken
from tijd import Tijden


INPUT_VAKKEN = "vakken.csv"
INPUT_ROOM = "data.rooms.csv"
INPUT_TIJDEN = "tijdslot.csv"
INPUT_OVERLAP = "overlapping.csv"

def open_room(INPUT_ROOM):
    """

    """
    #
    with open(INPUT_ROOM) as rooms:
        room_reader = csv.DictReader(rooms)
        #
        rooms = []
        for row in room_reader:
            number = row['Roomnumber']
            capacity = row['Max. capacity']
            room = Room(number, capacity)
            rooms.append(room)

        for i in range(len(rooms)):
        #     print(zalen[i].naam)
        #     print(zalen[i].capaciteit)
            print(rooms[i])

    return rooms

def open_vakken(INPUT_ZALEN):
    """
    Openen van de informatie van alle vakken.
    """

    # open Vakken
    with open(INPUT_VAKKEN) as vakken:
        vak_reader = csv.DictReader(vakken)
        # lijst met alle vakken
        vak_lijst = []
        for row in vak_reader:
            vak_naam = row['Vakken voor periode 4']
            vak_hc = row['#Hoorcolleges']
            vak_wc = row['#Werkcolleges']
            vak_pr = row['#Practica']
            vak = Vakken(vak_naam, vak_hc, vak_wc, vak_pr)
            vak_lijst.append(vak)

        for i in range(len(vak_lijst)):
            # print(vak_lijst[i].vak)
            # print(vak_lijst[i].vak_hc)
            # print(vak_lijst[i].vak_wc)
            # print(vak_lijst[i].vak_pr)
            print(vak_lijst[i])

    return vak_lijst


def open_overlapping(INPUT_OVERLAP):

    # open overlapping
    with open(INPUT_OVERLAP) as overlap:
        overlap_reader = csv.DictReader(overlap)

        # lijst met alle zalen
        data_dict = {}
        dubbelen = []

        for row in overlap_reader:
            vak = row['0']
            for i in row:
                if not row[i]:
                    continue
                elif row[i] != row['0']:
                    dubbelen.append(row[i])
            data_dict[vak] = dubbelen
            dubbelen = []

        print(data_dict)


    #     for i in range(len(zalen)):
    #     #     print(zalen[i].naam)
    #     #     print(zalen[i].capaciteit)
    #         print(zalen[i])
    #
    return data_dict

def main(INPUT_ROOM, INPUT_VAKKEN, INPUT_OVERLAP):
    """

    """
    rooms = open_room(INPUT_ROOM)

    vak_lijst = open_vakken(INPUT_VAKKEN)

    data_dict = open_overlapping(INPUT_OVERLAP)




if __name__ == "__main__":
    main(INPUT_ROOM, INPUT_VAKKEN, INPUT_TIJDEN, INPUT_OVERLAP)
