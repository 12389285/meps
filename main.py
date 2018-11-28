#
# MEPS Lecture making
# Main file
# by Eefje Roelfsema, Max Simons and Pascalle Veltman
#

import csv
import sys

# sys.path.insert(0, 'code/classes/')
from code.classes.room import Room
from code.classes.courses import Courses
import code.algorithms.basic_algorithm as ba
import code.algorithms.random_algorithm_B as rdb
from code.classes.schedule import Schedule

class Main():

    def __init__(self):
        self.rooms = self.open_room("data/rooms.csv")
        self.courses = self.open_courses("data/courses.csv")
        self.overlap = self.open_overlapping("data/overlapping.csv")
        self.sched = Schedule()
        self.schedule = self.sched.create()

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
                name = row['\ufeffCourses Period 4']
                lec = row['#lec']
                tut = row['#tut']
                prac = row['#pr']
                tut_tot = row['#tuttot']
                prac_tot = row['#prtot']
                max_tut = row['#max stud tut']
                max_prac = row['#max stud pr']
                exp_stud = row['E(students)']
                act_tot = int(row['#lec']) + int(row['#tuttot']) + int(row['#prtot'])
                course = Courses(name, lec, tut, prac, tut_tot, prac_tot, max_tut, max_prac, exp_stud, act_tot)
                course_list.append(course)

            for i in range(len(course_list)):
                lecs = int(course_list[i].lec)
                if lecs > 0:
                    for j in range(lecs):
                        activity = course_list[i].name
                        activity = activity + '_lec' + str(j+1)
                        course_list[i].add(activity)
                tuts = int(course_list[i].tut_tot)
                if tuts > 0:
                    for k in range(tuts):
                        activity = course_list[i].name
                        activity = activity + '_tut' + str(k+1)
                        course_list[i].add(activity)
                pracs = int(course_list[i].prac_tot)
                if pracs > 0:
                    for l in range(pracs):
                        activity = course_list[i].name
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
                    dubbels.append(row[i])
                overlap_dict[course] = dubbels
                dubbels = []

        return overlap_dict

    def fill_schedule(self):
        print(self.schedule[1][2][4])
        #aanpassing


if __name__ == "__main__":
    main = Main()
    overlap_dict = main.overlap
    schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # (rdb.list(main.courses, main.schedule, dict))
