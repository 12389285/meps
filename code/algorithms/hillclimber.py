from .scorefunction import scorefunction
import random

def hillclimber(schedule, number_swaps, rooms, courses, overlap_dict):
    day_lock1 = random.randint(0, 4)
    time_lock1 = random.randint(0, 4)
    room_lock1 = random.randint(0, 6)
    if time_lock1 == 4:
        room_lock1 = 0
    else:
        room_lock1 = random.randint(0, 6)

    day_lock2 = random.randint(0, 4)
    time_lock2 = random.randint(0, 4)
    if time_lock2 == 4:
        room_lock2 = 0
    else:
        room_lock2 = random.randint(0, 6)

    schedule1 = schedule

    activity1 = schedule[day_lock1][time_lock1][room_lock1]
    activity2 = schedule[day_lock2][time_lock2][room_lock2]

    schedule2 = schedule

    if overlapping(course, schedule[day_lock1][time_lock1])
        schedule2[day_lock2][time_lock2][room_lock2] = course1



    schedule2[day_lock1][time_lock1][room_lock1] = course2

    print(day_lock1, time_lock1, room_lock1, day_lock2, time_lock2, room_lock2)
