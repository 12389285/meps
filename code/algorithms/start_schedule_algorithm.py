from code.constraints.overlap import overlapping
from code.constraints.order import order
from .scorefunction import scorefunction
import operator
from operator import attrgetter
from random import shuffle

def create_start_schedule(courses, schedule, rooms, overlap_dict):
    """
    This function returns a schedule that satisfies the hard constraints.

    This function takes as input arguments:
        - list of Courses
        - empty schedule
        - list of rooms
        - overlap matrix

    This function works as follows:
        - puts activity of queue one by one in first possible room day_lock
    """

    queue = lecfirst_random_queue(courses)

    # check if queue is not empy
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

    return(schedule)

def lecfirst_random_queue(courses):
    """
    This function returns a queue:
        - first all lectures of the courses in random order
        - after that all tutorials and practica in random order
    """

    # create first queue which still is alphabetic
    alphab_queue = alphabetic_queue(courses)

    lectures = []
    others = []
    queue = []

    # seperate the lectures from other activities in lists
    for i in range(len(alphab_queue)):
        if '_lec' in alphab_queue[i]:
            lectures.append(alphab_queue[i])
        else:
            others.append(alphab_queue[i])

    # randomize the order
    shuffle(lectures)
    shuffle(others)

    # create queue woth lectures first
    for i in range(len(lectures)):
        queue.append(lectures[i])

    for i in range(len(others)):
        queue.append(others[i])

    return queue

def alphabetic_queue(courses):
    """
    This function returns a queue of all activities in alphabetic order.
    """

    alphab_queue = []

    for course in courses:
        for i in range(len(course.activities)):
            alphab_queue.append(course.activities[i])

    return(alphab_queue)
