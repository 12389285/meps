#
# random algorithm
#

from code.constraints.overlap import overlapping
from code.constraints.capacity import capacity
from code.constraints.queue import alphabetic_queue
from code.constraints.queue import lecfirst_queue
from code.constraints.queue import length_queue
from code.constraints.queue import random_queue
from code.constraints.order import order
from .scorefunction import scorefunction
from random import randint

def make_queue(courses, schedule, rooms, overlap_dict):

    queue = lecfirst_queue(courses)

    print(queue)

    return(random_schedule(courses, schedule, rooms, overlap_dict, queue))

def random_schedule(courses, schedule, rooms, overlap_dict, queue):

    for i in range(len(queue)):

        cont = 0

        print(queue[i])

        while cont == 0:

            day = randint(0,4)
            time = randint(0,4)
            if time == 4:
                room = 0
            else:
                room = randint(0,6)

            if schedule[day][time][room] == None:
                if overlapping(queue[i],schedule[day][time], overlap_dict):
                    if order(schedule, queue[i], day, time, queue):
                        schedule[day][time][room] = queue[i]
                        cont = 1
                        print('done!')

            else:
                cont = 0

    print(schedule)

    print(scorefunction(schedule, rooms, courses))

    return(schedule)
