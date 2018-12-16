# Meps lectures
# Eefje Roelsema – 10993673
# Pascalle Veltman – 11025646
# Max Simons – 12389285
# Main function to serve all other classes and funtions.

import csv
import sys
import time

# sys.path.insert(0, 'code/classes/')
from code.classes.room import Room
from code.classes.courses import Courses
<<<<<<< HEAD
import code.algorithms.basic_algorithm as ba
=======
import code.algorithms.start_schedule_algorithm as sa
>>>>>>> f732e5c5aa5743b205b1111c6950b2e6c2e7be9d
from code.classes.schedule import Schedule
from code.algorithms.hillclimber import hillclimber
from code.schedule.schedulemaker import csvconverter
from code.algorithms.simulated_annealing_deterministisch import simulated_annealing_deterministisch
from code.algorithms.scorefunction2 import scorefunction2
from code.algorithms.hillclimber_deterministisch import hillclimber_deterministisch
from code.algorithms.simulated_annealing import simulated_annealing
<<<<<<< HEAD
from code.algorithms.algorithm_deterministic import algorithm
=======
from code.constraints.couple import couples
>>>>>>> f732e5c5aa5743b205b1111c6950b2e6c2e7be9d


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
    print(sys.argv)
    algorithm = sys.argv[1]
    if len(sys.argv) > 2:
        number_swaps = sys.argv[2]

    if algorithm == 'hillclimber' or algorithm == 'simulated_annealing':
        # queue = input('Queue for start schedule: ')
        schedule = sa.create_start_schedule(main.courses, main.schedule, main.rooms, overlap_dict)
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

<<<<<<< HEAD
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
    schedule = simulated_annealing_deterministisch(main.courses, main.schedule, main.rooms, overlap_dict)
    # print(main.schedule)
    # schedule = (ba.make_queue(main.courses, main.schedule, main.rooms, overlap_dict))
    # schedule = hillclimber(schedule, 100000, main.rooms, main.courses, overlap_dict)
    # schedule = algorithm(main.courses, main.schedule, main.rooms, overlap_dict, True)

    # csvconverter(schedule_best)
    # print(overlap_dict)
    # schedule = hillclimber_determin(main.courses, main.schedule, main.rooms, overlap_dict)
    # schedule_best = simulated_annealing(schedule, 100000, main.rooms, main.courses, overlap_dict )
=======
>>>>>>> f732e5c5aa5743b205b1111c6950b2e6c2e7be9d
    print(schedule)
