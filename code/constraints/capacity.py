from code.classes.room import Room
from code.classes.courses import Courses
from main import Main

def capacity(course, room, courses):
    #checks if course can be given in that room, looking at capacity

    course_kind, activity_kind = course.split("_")

    for i in range(len(courses)):
        if course_kind in courses[i].course_name:
            if 'lec' in activity_kind:
                students_activity = courses[i].course_expstud
            elif 'tut' in activity_kind:
                students_activity = courses[i].course_maxtut
            elif 'prac' in activity_kind:
                students_activity = courses[i].course_maxprac

    room_capacity = room.capacity
    print(room_capacity)
    print(students_activity)

    if int(room_capacity) < int(students_activity):
        return False
    else:
        return True
