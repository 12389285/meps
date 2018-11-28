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

<<<<<<< HEAD
    return queue
=======
    return(queue)
>>>>>>> f1a4a1f9b2f4f3d28e88b030492fda5e63eda0a5

def length_queue(courses):

    courses.sort(key=lambda x: x.act_tot)
    courses = list(reversed(courses))

    queue = []

    for course in courses:
        for i in range(len(course.activities)):
            queue.append(course.activities[i])

    return queue
