#
# MEPS Lecture making
# Main file
# by Eefje Roelfsema, Max Simons and Pascalle Veltman
#

import csv
import sys
import time

# sys.path.insert(0, 'code/classes/')
from code.classes.room import Room
from code.classes.courses import Courses
import code.algorithms.basic_algorithm as ba
import code.algorithms.random_algorithm_B as rdb
from code.classes.schedule import Schedule
from code.algorithms.hillclimber import hillclimber
from code.schedule.schedulemaker import csvconverter
from code.algorithms.simulated_annealing import simulated_annealing
from code.algorithms.scorefunction2 import scorefunction2

class Main():

    def __init__(self):
        self.rooms = self.open_room("data/rooms.csv")
        self.courses = self.open_courses("data/courses.csv")
        self.overlap = self.open_overlapping("data/overlapping.csv")
        self.sched = Schedule()
        self.schedule = self.sched.create()
        self.simulated = self.make_list("data/courses.csv")

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
                dif_total = int(row['#lec']) + int(row['#tut']) + int(row['#pr'])
                act_tot = int(row['#lec']) + int(row['#tuttot']) + int(row['#prtot'])
                course = Courses(name, lec, tut, prac, tut_tot, prac_tot, max_tut, max_prac, exp_stud, act_tot, dif_total)
                course_list.append(course)

                course_list_simulated = []

            for i in range(len(course_list)):
                lecs = int(course_list[i].lec)
                course_list_simulated.append(course_list[i].name + '_lec')
                if lecs > 0:
                    for j in range(lecs):
                        activity = course_list[i].name
                        activity = activity + '_lec'
                        course_list[i].add(activity)
                tuts = int(course_list[i].tut_tot)
                if tuts > 0:
                    course_list_simulated.append(course_list[i].name + '_tut')
                    for k in range(tuts):
                        activity = course_list[i].name
                        activity = activity + '_tut'
                        course_list[i].add(activity)
                pracs = int(course_list[i].prac_tot)
                if pracs > 0:
                    course_list_simulated.append(course_list[i].name + '_prac')
                    for l in range(pracs):
                        activity = course_list[i].name
                        activity = activity + '_prac'
                        course_list[i].add(activity)


        return course_list

    def make_list(self, filename):
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
                dif_total = int(row['#lec']) + int(row['#tut']) + int(row['#pr'])
                course = Courses(name, lec, tut, prac, tut_tot, prac_tot, max_tut, max_prac, exp_stud, act_tot, dif_total)
                course_list.append(course)

                course_list_simulated = []

            for i in range(len(course_list)):
                lecs = int(course_list[i].lec)
                course_list_simulated.append(course_list[i].name + '_lec')
                if lecs > 0:
                    for j in range(lecs):
                        activity = course_list[i].name
                        activity = activity + '_lec'
                        course_list[i].add(activity)
                tuts = int(course_list[i].tut_tot)
                if tuts > 0:
                    course_list_simulated.append(course_list[i].name + '_tut')
                    for k in range(tuts):
                        activity = course_list[i].name
                        activity = activity + '_tut'
                        course_list[i].add(activity)
                pracs = int(course_list[i].prac_tot)
                if pracs > 0:
                    course_list_simulated.append(course_list[i].name + '_prac')
                    for l in range(pracs):
                        activity = course_list[i].name
                        activity = activity + '_prac'
                        course_list[i].add(activity)


        return course_list_simulated

    def open_overlapping(self, filename):
        """

        """
        #
        with open(filename) as overlap:
            overlap_reader = csv.DictReader(overlap)


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

    # schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # start_time = time.time()
    # print("--- %s seconds ---" % (time.time() - start_time))
    schedule_best = simulated_annealing(main.courses, main.schedule, main.rooms, overlap_dict)
    # schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # schedule_best = hillclimber(schedule, 100000, main.rooms, main.courses, overlap_dict)
    # csvconverter(schedule_best)


    # (rdb.list(main.courses, main.schedule, dict))
