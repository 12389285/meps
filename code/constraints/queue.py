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

    len_queue = length_queue(courses)

    lectures = []
    others = []

    for i in range(len(len_queue)):
        if '_lec' in len_queue[i]:
            lectures.append(len_queue[i])
        else:
            others.append(len_queue[i])

    queue = []
    queue.append(','.join(lectures))
    queue.append(','.join(others))

    return(queue)

def length_queue(courses):

    courses.sort(key=lambda x: x.act_tot)
    courses = list(reversed(courses))

    queue = []

    for course in courses:
        for i in range(len(course.activities)):
            queue.append(course.activities[i])

    return(queue)
