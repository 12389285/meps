#
# Hillclimber algorihm switches rendom activities
#
import math
import copy
from code.constraints.overlap import overlapping
from code.constraints.order import order
from code.constraints.distribution import distribution
from .scorefunction import scorefunction
import random

import matplotlib.pyplot as plt

def simulated_annealing(schedule, number_swaps, rooms, courses, overlap_dict):
    # set score-best to a infinte high number
    score_best = 100000
    # make copy of best schedule
    schedule_best = copy.deepcopy(schedule)
    # make lists needed
    score = []
    swaps = []
    # determine variables and set to 0
    swaps_num = 0
    temp_number = 0

    # iterate as many times as given when calling the function
    for i in range(number_swaps):
        # set temp beginning to 30
        temp = 30
        # when a certain amount of swaps is reached, make temp lower
        if temp_number == 100:
            temp_number = 0
            temp = temp * 0.85

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
        # swap the 2 random acitivities in the copied schedule
        schedule2[day_lock1][time_lock1][room_lock1] = None
        schedule2[day_lock2][time_lock2][room_lock2] = None


        works = 0
        # check if hard constraints are still satisfied (overlapping and order), for both swapped activities in schedule
        if overlapping(activity1, schedule2[day_lock2][time_lock2], overlap_dict):
            if order(schedule2, activity1, day_lock2, time_lock2):
                schedule2[day_lock2][time_lock2][room_lock2] = activity1
                if overlapping(activity2, schedule2[day_lock1][time_lock1], overlap_dict):
                    if order(schedule2, activity2, day_lock1, time_lock1):
                        schedule2[day_lock1][time_lock1][room_lock1] = activity2
                        works = 1
                        # if so move on, otherwise definitely no swap will occur
        sum = 0
        # if hard constraints are satisfied in new schedule (works is 1), calculate the scorefunction for new schedule
        if works == 1:
            score2 = scorefunction(schedule2, rooms, courses)
            # calculate e-scores
            e_score1 = math.exp(-score1/temp)
            e_score2 = math.exp(-score2/temp)
            # add both e-scores
            sum = e_score1 + e_score2
            # get a random number from uniform distribution 0-1
            probability = random.uniform(0,1)
            # calculate probability of choosing original schedule
            prob_1 = e_score1 / sum
            # if the probability of choosing original schedule is lower than probability of uniform distribution
            # choose to swap, otherwise keep original schedule
            if prob_1 < probability:
                    schedule = schedule2
                    # add temp_number with 1, needed to know when lowering temperature
                    temp_number += 1

        # data for plot show
        swaps_num += 1
        swaps.append(swaps_num)
        score_data = scorefunction(schedule, rooms, courses)
        score.append(score_data)

        if score_data < score_best:
            schedule_best = schedule
            score_best = score_data


        print(f"score:", score_data)
        print(f"best:", score_best)

        print(scorefunction(schedule, rooms, courses))

    # print(schedule)
    # # plot show of maluspoints
    # plt.plot(swaps, score)
    # plt.axis([0, max(swaps), 0, max(score) + 50])
    # plt.text(max(swaps) + 1, min(score), min(score))
    # plt.title('Hillclimber algorithm')
    # plt.xlabel('Number of swaps')
    # plt.ylabel('Malus points')
    # plt.show()

    return(schedule)
