#
#   Creates queue of activities
#   Returns queue list of all activities.
#

import operator
from operator import attrgetter
from random import shuffle

def alphabetic_queue(courses):
    # makes a queue of activities on alphabetic order

    alphab_queue = []

    for course in courses:
        for i in range(len(course.activities)):
            alphab_queue.append(course.activities[i])

    return(alphab_queue)

def lecfirst_queue(courses):
    # creates queue with all lecture activities first

    len_queue = length_queue(courses)

    lectures = []
    others = []
    queue = []

    for i in range(len(len_queue)):
        if '_lec' in len_queue[i]:
            lectures.append(len_queue[i])
        else:
            others.append(len_queue[i])

    for i in range(len(lectures)):
        queue.append(lectures[i])

    for i in range(len(others)):
        queue.append(others[i])

    return queue

def lecfirst_random_queue(courses):
    # creates a queue with lectures first in random order

    len_queue = length_queue(courses)

    lectures = []
    others = []
    queue = []

    for i in range(len(len_queue)):
        if '_lec' in len_queue[i]:
            lectures.append(len_queue[i])
        else:
            others.append(len_queue[i])

    shuffle(lectures)
    shuffle(others)

    for i in range(len(lectures)):
        queue.append(lectures[i])

    for i in range(len(others)):
        queue.append(others[i])

    return queue

def length_queue(courses):
    # creates a queue that puts courses with many activities first

    courses.sort(key=lambda x: x.act_tot)
    courses = list(reversed(courses))

    queue = []

    for course in courses:
        for i in range(len(course.activities)):
            queue.append(course.activities[i])

    return queue

def random_queue(courses):
    # creates a total random queue of all activities

    queue = alphabetic_queue(courses)

    shuffle(queue)

    return(queue)
