#
#   Checks if course can be given in that room, looking at capacity.
#   Returns True or False
#

from code.classes.room import Room
from code.classes.courses import Courses

def capacity(course, room, courses):

    course_kind, activity_kind = course.split("_")

    for i in range(len(courses)):
        if course_kind == courses[i].name:
            if 'lec' in activity_kind:
                students_activity = courses[i].exp_stud
            elif 'tut' in activity_kind:
                students_activity = courses[i].max_tut
            elif 'prac' in activity_kind:
                students_activity = courses[i].max_prac
            else:
                print('not found')

    room_capacity = room.capacity
    #
    # if int(room_capacity) < int(students_activity):
    #     return False
    # else:
    #     return True

    # scoreboard maluspunten
    malus = 0

    if int(room_capacity) < int(students_activity):
        malus = malus + int(students_activity) - int(room_capacity)
        return malus
    else:
        return malus
