import csv
import sys

# sys.path.insert(0, 'code/classes/')
from code.classes.room import Room
from code.classes.courses import Courses
import code.algorithms.random_algorithm as rd
import code.algorithms.random_algorithm_B as rdb
from code.classes.schedule import Schedule

class Main():

    def __init__(self):
        self.rooms = self.open_room("data/rooms.csv")
        self.courses = self.open_courses("data/courses.csv")
        self.overlap = self.open_overlapping("data/overlapping.csv")
        self.schedule = Schedule()
        self.empty = self.schedule.create()

    def open_room(self, filename):
        """

        """
        with open(filename) as rooms:
            room_reader = csv.DictReader(rooms)
            rooms = []
            for row in room_reader:
                number = row['Roomnumber']
                capacity = row['Max. capacity']
                room = Room(number, capacity)
                rooms.append(room)

        return rooms

    def open_courses(self, filename):
        """

        """

        with open(filename) as courses:
            course_reader = csv.DictReader(courses)
            course_list = []
            for row in course_reader:
                course_name = row['\ufeffCourses Period 4']
                course_lec = row['#lec']
                course_tut = row['#tut']
                course_prac = row['#pr']
                course_tuttot = row['#tuttot']
                course_practot = row['#prtot']
                course_maxtut = row['#max stud tut']
                course_maxprac = row['#max stud pr']
                course_expstud = row['E(students)']
                course = Courses(course_name, course_lec, course_tut, course_prac, course_tuttot, course_practot, course_maxtut, course_maxprac, course_expstud)
                course_list.append(course)

            for i in range(len(course_list)):
                lecs = int(course_list[i].course_lec)
                if lecs > 0:
                    for j in range(lecs):
                        activity = course_list[i].course_name
                        activity = activity + '_lec' + str(j+1)
                        course_list[i].add(activity)
                tuts = int(course_list[i].course_tuttot)
                if tuts > 0:
                    for k in range(tuts):
                        activity = course_list[i].course_name
                        activity = activity + '_tut' + str(k+1)
                        course_list[i].add(activity)
                pracs = int(course_list[i].course_practot)
                if pracs > 0:
                    for l in range(pracs):
                        activity = course_list[i].course_name
                        activity = activity + '_prac' + str(l+1)
                        course_list[i].add(activity)

        return course_list


    def open_overlapping(self, filename):
        """

        """
        #
        with open(filename) as overlap:
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

        return overlap_dict


    def fill_schedule(self):
        print(self.empty[1][2][4])
        #aanpassing


if __name__ == "__main__":
    main = Main()
    overlap_dict = main.overlap
    (rd.list(main.courses, main.empty, main.rooms, overlap_dict))
    # (rdb.list(main.courses, main.empty, dict))
