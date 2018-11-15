
import csv
from room import Room
from courses import Courses

INPUT_COURSES = "data.courses.csv"
INPUT_ROOM = "data.rooms.csv"
INPUT_OVERLAP = "data.overlapping.csv"

def open_room(INPUT_ROOM):
    """

    """
    with open(INPUT_ROOM) as rooms:
        room_reader = csv.DictReader(rooms)
        rooms = []
        for row in room_reader:
            number = row['Roomnumber']
            capacity = row['Max. capacity']
            room = Room(number, capacity)
            rooms.append(room)

        for i in range(len(rooms)):
            print(rooms[i])

    return rooms

def open_courses(INPUT_COURSES):
    """

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
    """

    """

    #
    with open(INPUT_OVERLAP) as overlap:
        overlap_reader = csv.DictReader(overlap)

        #
        overlap_dict = {}
        dubbels = []

        for row in overlap_reader:
            course = row['0']
            for i in row:
                if not row[i]:
                    continue
                elif row[i] != row['0']:
                    dubbels.append(row[i])
            overlap_dict[vak] = dubbels
            dubbels = []

        print(overlap_dict)


    #     for i in range(len(zalen)):
    #     #     print(zalen[i].naam)
    #     #     print(zalen[i].capaciteit)
    #         print(zalen[i])
    #
    return overlap_dict

def load(INPUT_ROOM, INPUT_COURSES, INPUT_OVERLAP):
    """

    """
    rooms = open_room(INPUT_ROOM)

    course_list = open_courses(INPUT_COURSES)

    overlap_dict = open_overlapping(INPUT_OVERLAP)




if __name__ == "__main__":
    load(INPUT_ROOM, INPUT_COURSES, INPUT_OVERLAP)
