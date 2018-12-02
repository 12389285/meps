#
# Hillclimber algorihm switches rendom activities
#

import copy
from code.constraints.overlap import overlapping
from code.constraints.order import order
from .scorefunction import scorefunction
import random
import matplotlib.pyplot as plt

def hillclimber(schedule, number_swaps, rooms, courses, overlap_dict):
    score = []
    swaps = []
    swaps_num = 0
    for i in range(number_swaps):

        score1 = scorefunction(schedule, rooms, courses)
        print(score1)

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


        activity1 = schedule[day_lock1][time_lock1][room_lock1]
        activity2 = schedule[day_lock2][time_lock2][room_lock2]

        schedule2 = copy.deepcopy(schedule)
        schedule2[day_lock1][time_lock1][room_lock1] = None
        schedule2[day_lock2][time_lock2][room_lock2] = None


        works = 0

        if overlapping(activity1, schedule2[day_lock2][time_lock2], overlap_dict):
            if order(schedule2, activity1, day_lock2, time_lock2):
                schedule2[day_lock2][time_lock2][room_lock2] = activity1
                if overlapping(activity2, schedule2[day_lock1][time_lock1], overlap_dict):
                    if order(schedule2, activity2, day_lock1, time_lock1):
                        schedule2[day_lock1][time_lock1][room_lock1] = activity2
                        works = 1

        if works == 1:
            score1 = scorefunction(schedule, rooms, courses)
            score2 = scorefunction(schedule2, rooms, courses)
            if score2 < score1:
                schedule = schedule2
                print('switched!')
        else:
            print('no switch :(')

        # data for plot show
        swaps_num += 1
        swaps.append(swaps_num)
        score_data = scorefunction(schedule, rooms, courses)
        score.append(score_data)

        print(scorefunction(schedule, rooms, courses))

    # plot show of maluspoints
    plt.plot(swaps, score)
    plt.axis([0, max(swaps), 0, max(score) + 50])
    plt.text(max(swaps) + 1, min(score), min(score))
    plt.title('Hillclimber algorithm')
    plt.xlabel('Number of swaps')
    plt.ylabel('Malus points')
    plt.show()

    print(schedule)

    return(schedule)
