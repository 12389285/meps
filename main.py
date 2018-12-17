import csv
import sys
import time

from code.classes.room import Room
from code.classes.courses import Courses
from code.algorithms.start_schedule_algorithm import create_start_schedule as sa
from code.classes.schedule import Schedule
from code.algorithms.hillclimber import hillclimber
from code.schedule.schedulemaker import csvconverter
from code.algorithms.simulated_annealing_deterministisch import simulated_annealing_deterministisch
from code.algorithms.scorefunction_deterministic import scorefunction_deterministic
from code.algorithms.hillclimber_deterministisch import hillclimber_deterministisch
from code.algorithms.simulated_annealing import simulated_annealing
from code.constraints.couple import couples
from code.algorithms.algorithm_deterministic import algorithm as algorithm_deterministic
from code.algorithms.algorithm import algorithm
from code.algorithms.scorefunction_show import scorefunction_show


class Main():

    def __init__(self):
        self.rooms = self.open_room("data/rooms.csv")
        self.courses = self.open_courses("data/courses.csv")
        self.overlap = self.open_overlapping("data/overlapping.csv")
        self.sched = Schedule()
        self.schedule = self.sched.create()

    def open_room(self, filename):
        """
        This function opens all the room from a csv file and returns a list.
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
        This function opens all the courses from a csv file and returns a cours
        list. The function also puts the courses order of amount of activities
        in the activity list.
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


    def open_overlapping(self, filename):

        """
        This function opens a csv file with the overlapping of courses and retruns
        a list.
        """

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

        """
        This function fills an empty schedule.
        """

        print(self.schedule[1][2][4])


if __name__ == "__main__":
    main = Main()
    overlap_dict = main.overlap
    print(sys.argv)
    algorithm = sys.argv[1]
    if len(sys.argv) > 2:
        number_swaps = sys.argv[2]

    if algorithm == 'hillclimber' or algorithm == 'simulated_annealing':
        # queue = input('Queue for start schedule: ')
        schedule = sa(main.courses, main.schedule, main.rooms, overlap_dict)
        if algorithm == 'hillclimber':
            schedule = hillclimber(schedule, int(number_swaps), main.rooms, main.courses, overlap_dict)
        elif algorithm == 'simulated_annealing':
            schedule = simulated_annealing(schedule, int(number_swaps), main.rooms, main.courses, overlap_dict)
    elif algorithm == 'simulated_annealing_deterministisch':
        schedule = simulated_annealing_deterministisch(main.courses, main.schedule, main.rooms, overlap_dict)
    elif algorithm == 'hillclimber_deterministisch':
        schedule = hillclimber_deterministisch(main.courses, main.schedule, main.rooms, overlap_dict)
    else:
        print('Algorithm does not exist.')

    # schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # start_time = time.time()
    # print("--- %s seconds ---" % (time.time() - start_time))
    # schedule_best = simulated_annealing(main.courses, main.schedule, main.rooms, overlap_dict)
    # schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # schedule_best = hillclimber(schedule, 100000, main.rooms, main.courses, overlap_dict)
    # schedule_best = simulated_annealing_deterministisch(main.courses, main.schedule, main.rooms, overlap_dict)
    # print(main.schedule)
    # schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # schedule_best = hillclimber(schedule, 10000, main.rooms, main.courses, overlap_dict)
    # csvconverter(schedule_best)
    # print(overlap_dict)
    # schedule = hillclimber_determin(main.courses, main.schedule, main.rooms, overlap_dict)
    # schedule_best = simulated_annealing(schedule, 200000, main.rooms, main.courses, overlap_dict )
    # csvconverter(schedule_best)
    # schedule_best = hillclimber(schedule, 10000, main.rooms, main.courses, overlap_dict)
    # schedule = simulated_annealing_deterministisch(main.courses, main.schedule, main.rooms, overlap_dict)
    # print(main.schedule)
    # schedule = sa(main.courses, main.schedule, main.rooms, overlap_dict)
    # schedule = hillclimber(schedule, 100000, main.rooms, main.courses, overlap_dict)
    # schedule = algorithm_deterministic(main.courses, main.schedule, main.rooms, overlap_dict, True)
    # schedule = algorithm(schedule, 100000, main.rooms, main.courses, overlap_dict,True)
    # scorefunction_show(schedule, main.courses, main.rooms, overlap_dict)
    # csvconverter(schedule_best)
    # print(overlap_dict)
    # schedule = hillclimber_determin(main.courses, main.schedule, main.rooms, overlap_dict)
    # schedule_best = simulated_annealing(schedule, 100000, main.rooms,s main.courses, overlap_dict )
    # print(schedule)
