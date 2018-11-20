
import csv
import sys

sys.path.insert(0, 'code/classes/')
from room import Room
from courses import Courses

INPUT_COURSES = "data/courses.csv"
INPUT_ROOM = "data/rooms.csv"
INPUT_OVERLAP = "data/overlapping.csv"

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
    #
    with open(INPUT_COURSES) as courses:
        course_reader = csv.DictReader(courses)
        #
        course_list = []
        for row in course_reader:
            course_name = row['Vakken voor periode 4']
            course_lec = row['#Hoorcolleges']
            course_tut = row['#Werkcolleges']
            course_prac = row['#Practica']
            course = Courses(course_name, course_lec, course_tut, course_prac)
            course_list.append(course)

        for i in range(len(course_list)):
            lecs = int(course_list[i].course_lec)
            if lecs > 0:
                for j in range(lecs):
                    activity = course_list[i].course_name
                    activity = activity + ' lec' + str(j+1)
                    course_list[i].add(activity)
            tuts = int(course_list[i].course_tut)
            if tuts > 0:
                for k in range(tuts):
                    activity = course_list[i].course_name
                    activity = activity + ' tut' + str(k+1)
                    course_list[i].add(activity)
            pracs = int(course_list[i].course_prac)
            if pracs > 0:
                for l in range(pracs):
                    activity = course_list[i].course_name
                    activity = activity + ' prac' + str(l+1)
                    course_list[i].add(activity)
            print(course_list[i].activities)

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
            overlap_dict[course] = dubbels
            dubbels = []

        print(overlap_dict)

    return overlap_dict

def load(INPUT_ROOM, INPUT_COURSES, INPUT_OVERLAP):
    """

    """
    rooms = open_room(INPUT_ROOM)

    course_list = open_courses(INPUT_COURSES)

    overlap_dict = open_overlapping(INPUT_OVERLAP)


if __name__ == "__main__":
    load(INPUT_ROOM, INPUT_COURSES, INPUT_OVERLAP)
