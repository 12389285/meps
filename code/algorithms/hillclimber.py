#
# Hillclimber algorihm switches random activities
#
import copy
from code.constraints.overlap import overlapping
from code.constraints.couple import couples
from code.constraints.order import order
from code.constraints.distribution import distribution
from .scorefunction import scorefunction
import random
import matplotlib.pyplot as plt

def hillclimber(schedule, number_swaps, rooms, courses, overlap_dict):
    # make lists needed
    score = []
    swaps = []
    # make variable and set to 0
    swaps_num = 0

    # start running hillclimber

    # iterate as many times as given when calling the function
    for i in range(number_swaps):

            # determine score of current schedule (hard constraints are satisfied, because that is dealt with by making the begin schedule)
        score1 = scorefunction(schedule, rooms, courses)

        # find random a daylock, timelock
        day_lock1 = random.randint(0, 4)
        time_lock1 = random.randint(0, 4)

        # if timelock is equal to 4, there is only 1 roomlock
        if time_lock1 == 4:
            room_lock1 = 0
        # else choose random timelock (0-6)
        else:
            room_lock1 = random.randint(0, 6)

        # find another random daylock2 and timelock2
        day_lock2 = random.randint(0, 4)
        time_lock2 = random.randint(0, 4)
        # if timelock is 4, roomlock2 is 0
        if time_lock2 == 4:
            room_lock2 = 0
        # else choose random timelock (0-6)
        else:
            room_lock2 = random.randint(0, 6)

        # find activities according to chosen daylocks, timelocks and roomlocks random
        activity1 = schedule[day_lock1][time_lock1][room_lock1]
        activity2 = schedule[day_lock2][time_lock2][room_lock2]

        # copy the schedule
        schedule2 = copy.deepcopy(schedule)
        # make the 2 roomlocks chosen None
        schedule2[day_lock1][time_lock1][room_lock1] = None
        schedule2[day_lock2][time_lock2][room_lock2] = None


        works = 0
        # check if hard constraints are still satisfied (overlapping and order), for both swapped activities in schedule
        # and if so swap in copied schedule        if overlapping(activity1, schedule2[day_lock2][time_lock2], overlap_dict):
        if order(schedule2, activity1, day_lock2, time_lock2):
            schedule2[day_lock2][time_lock2][room_lock2] = activity1
            if overlapping(activity2, schedule2[day_lock1][time_lock1], overlap_dict):
                if order(schedule2, activity2, day_lock1, time_lock1):
                    schedule2[day_lock1][time_lock1][room_lock1] = activity2
                    works = 1

        # if hard constraints are satisfied in new schedule (works is 1), calculate the scorefunction for new schedule
        if works == 1:
            # calculate swapped score
            score2 = scorefunction(schedule2, rooms, courses)
            if score2 < score1:
                # if score 2 is lower than score1 (better), new schedule is schedule2
                schedule = schedule2


        # data for plot show
        swaps_num += 1
        swaps.append(swaps_num)
        score_data = scorefunction(schedule, rooms, courses)
        score.append(score_data)

        # print(score_data)


    print(schedule)
    # plot show of maluspoints
    plt.plot(swaps, score)
    plt.axis([0, max(swaps), 0, max(score) + 50])
    plt.text(max(swaps) + 1, min(score), min(score))
    plt.title('Hillclimber algorithm')
    plt.xlabel('Number of swaps')
    plt.ylabel('Malus points')
    plt.show()

    return schedule
