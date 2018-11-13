
import csv
from room import Room
from vakken import Vakken
from tijd import Tijden


INPUT_COURSES = "courses.csv"
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

def open_courses(INPUT_COURSES):
    """
    Openen van de informatie van alle vakken.
    """

    # open Vakken
    with open(INPUT_COURSES) as courses:
        course_reader = csv.DictReader(courses)
        # lijst met alle vakken
        course_list = []
        for row in course_reader:
            course_name = row['Vakken voor periode 4']
            course_hc = row['#Hoorcolleges']
            course_wc = row['#Werkcolleges']
            course_pr = row['#Practica']
            course = Courses(course_name, course_hc, course_wc, course_pr)
            course_list.append(course)

        for i in range(len(course_list)):
            # print(vak_lijst[i].vak)
            # print(vak_lijst[i].vak_hc)
            # print(vak_lijst[i].vak_wc)
            # print(vak_lijst[i].vak_pr)
            print(course_list[i])

    return course_list


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
