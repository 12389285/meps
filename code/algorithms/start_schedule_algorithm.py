#
#   Algorithm for create schedule by queue
#
from code.constraints.overlap import overlapping
from code.constraints.capacity import capacity
from code.constraints.order import order
from .scorefunction import scorefunction
import operator
from operator import attrgetter
from random import shuffle

def create_start_schedule(courses, schedule, rooms, overlap_dict):

    queue = lecfirst_random_queue(courses)

    i = 0
    # check if queue is not empy
    malus = 0

    while queue != []:
        # select day i
        for i in range(len(schedule)):
            # select timelock j
            for j in range(len(schedule[i])):
                # select room lock k
                for k in range(len(schedule[i][j])):
                    if schedule[i][j][k] is None:
                        for l in range(len(queue)):
                            if overlapping(queue[l],schedule[i][j], overlap_dict):
                                if order(schedule, queue[l], i, j):
                                    schedule[i][j][k] = queue[l]
                                    queue.remove(queue[l])
                                    break
                                else:
                                    continue
                            else:
                                continue

    print(scorefunction(schedule, rooms, courses))
    return(schedule)

def lecfirst_random_queue(courses):
    # creates a queue with lectures first in random order

    alphabetic_queue = []

    for course in courses:
        for i in range(len(course.activities)):
            alphabetic_queue.append(course.activities[i])

    lectures = []
    others = []
    queue = []

    for i in range(len(alphabetic_queue)):
        if '_lec' in alphabetic_queue[i]:
            lectures.append(alphabetic_queue[i])
        else:
            others.append(alphabetic_queue[i])

    shuffle(lectures)
    shuffle(others)

    for i in range(len(lectures)):
        queue.append(lectures[i])

    for i in range(len(others)):
        queue.append(others[i])

    return queue
