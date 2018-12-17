from code.classes.room import Room
from code.classes.courses import Courses

def capacity(course, room, courses):
    """
    This function returns the malus points of students not fitting
    into a room.

    This function takes as input arguments:
        - the course activity
        - the room in which the course is given
        - the list of all courses

    This function works as follows:
        - it determines how many students are at the activity
        - it calculates how many students do not fit in the rooms
    """

    # split input into course and activity kind
    if course != None:
        course_kind, activity_kind = course.split("_")

    # find the amount of students at activity
    if course != None:
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

        # calculate difference between capacity and amount of students
        room_capacity = room.capacity
        malus = 0
        if int(room_capacity) < int(students_activity):
            malus = malus + int(students_activity) - int(room_capacity)
            return malus
        else:
            return malus
    else:
        return 0
