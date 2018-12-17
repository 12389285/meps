import math
import copy
from code.constraints.overlap import overlapping
from code.constraints.order import order
from code.constraints.distribution import distribution
from .scorefunction import scorefunction
import random

def algorithm(schedule, number_iterations, rooms, courses, overlap_dict, simulated_annealing_true):

    score = []
    swaps = []
    swaps_num = 0

    for i in range(number_iterations):
        score_current = scorefunction(schedule, rooms, courses)

        daylock1, timelock1, roomlock1 = random_numbers()
        daylock2, timelock2, roomlock2 = random_numbers()
        activity1 = schedule[day_lock1][time_lock1][room_lock1]
        activity2 = schedule[day_lock2][time_lock2][room_lock2]

        schedule_swap = copy.deepcopy(schedule)

        schedule_swap[day_lock1][time_lock1][room_lock1] = None
        schedule_swap[day_lock2][time_lock2][room_lock2] = None

        if hard_constraints == True:
            schedule_swap[day_lock1][time_lock1][room_lock1] = activity2
            schedule_swap[day_lock2][time_lock2][roomlock_2] = activity1
            score_swap = scorefunction(schedule_swap, rooms, courses)
            if simulated_annealing_true == True:
                schedule = simulated_annealing(schedule, schedule_swap, temp, score_current, score_swap)

            else:
                schedule = hillclimber(schedule, schedule_swap, score_current, score_swap)

def random_numbers():

    day_lock = random.randint(0, 4)
    time_lock = random.randint(0, 4)

    if time_lock == 4:
        room_lock = 0
    else:
        room_lock = random.randint(0, 6)

    return [day_lock, timelock, room_lock]

def hard_constraints():

    if order(schedule_swap, activity1, day_lock2, time_lock2):
        schedule_swap[day_lock2][time_lock2][room_lock2] = activity1
        if overlapping(activity2, schedule_swap[day_lock1][time_lock1], overlap_dict):
            if order(schedule_swap, activity2, day_lock1, time_lock1):
                schedule_swap[day_lock1][time_lock1][room_lock1] = activity2
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def simulated_annealing(schedule, schedule_swap, temp, score_current, score_swap):
    e_score_current = (-score_current / temp)
    e_score_swap = (-score_swap / temp)
    e_score_sum = e_score_current + e_score_swap

    probability = random.uniform(0,1)
    prob_current = e_score_current / e_score_sum

    if prob_current < probability:
        return schedule
    else:
        return schedule_swap

def hillclimber(schedule, schedule_swap, score_current, score_swap):
    if score_current < score_swap:
        return schedule
    else:
        return schedule_swap


Pseudocode: nog temp bekijken.
