#
#   Creates queue of activities
#   Returns queue list of all activities.
#

import operator
from operator import attrgetter

def alphabetic_queue(courses):

    alphab_queue = []

    for course in courses:
        for i in range(len(course.activities)):
            alphab_queue.append(course.activities[i])

    return(alphab_queue)

def lecfirst_queue(courses):

    alphab_queue = alphabetic_queue(courses)

    lectures = []
    others = []

    for i in range(len(alphab_queue)):
        if '_lec' in alphab_queue[i]:
            lectures.append(alphab_queue[i])
        else:
            others.append(alphab_queue[i])

    queue = []
    queue.append(','.join(lectures))
    queue.append(','.join(others))

    return(queue)

# def length_queue(courses):
#
#     courses = sorted(courses, key=)
