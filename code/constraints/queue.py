#
#   Creates queue of activities
#   Returns queue list of all activities.
#

import operator
from operator import attrgetter
from random import shuffle

def alphabetic_queue(courses):

    alphabetic_queue = []

    for course in courses:
        for i in range(len(course.activities)):
            alphabetic_queue.append(course.activities[i])

    return(alphabetic_queue)


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
