import math
import copy
from code.constraints.overlap import overlapping
from code.constraints.order import order
from code.constraints.distribution import distribution
from .scorefunction import scorefunction
from .plot import plot_scores
import random

def algorithm(schedule, number_iterations, rooms, courses, overlap_dict, simulated_annealing_true):
    """""
    This algorithm runs the non-deterministic algorithms

    This function takes as input arguments:
        - the filled in schedule (hard constraints are satisfied, but furthermore not an optimal schedule)
        - the number of iterations requested by the user
        - the roomlist
        - the courselist (classes)
        - the overlapping dictionary
        - boolean for Simulated Annealing or Hillclimber (boolean)


    This function works as follows:
    - Saves the current score and current schedule
    - It sets the temperature and number of swaps and makes a scoreplotlist
    - It then iterates as many times as the user requests

    - The current score of the scorefunction is calculated
    - It picks 2 random activities (by picking a day, a timelock and a roomlock)
    - It makes a copy of the current schedule to store the swap schedule and makes both chosen roomlocks None
    - It checks if swapping the 2 activities satisfies the hard constraints

    - If the user instructed simulated annealing:
    - If 1000 times simulated function is called, the temperature drops
    - The simulated annealing function is called to determine if the schedule is swapped
    - The new score is calculated, new_score and schedule are saved if new score is lower than the best old score
    -

    - If the user instructed the hillclimber:
    - The hillclimber function determines if the schedule is swapped and the schedule is saved in schedule_save
    """""

    score_save = scorefunction(schedule, rooms, courses)
    schedule_save = copy.deepcopy(schedule)
    temp_number = 0
    swaps_number = 0
    temp = 20
    score_plot_list = []

    for i in range(number_iterations):
        score_current = scorefunction(schedule, rooms, courses)
        daylock1, timelock1, roomlock1 = random_numbers()
        daylock2, timelock2, roomlock2 = random_numbers()
        activity1 = schedule[daylock1][timelock1][roomlock1]
        activity2 = schedule[daylock2][timelock2][roomlock2]

        schedule_swap = copy.deepcopy(schedule)

        schedule_swap[daylock1][timelock1][roomlock1] = None
        schedule_swap[daylock2][timelock2][roomlock2] = None

        if hard_constraints(schedule_swap, overlap_dict, activity1, activity2, daylock1, daylock2, timelock1, timelock2, roomlock1, roomlock2) == True:
            schedule_swap[daylock1][timelock1][roomlock1] = activity2
            schedule_swap[daylock2][timelock2][roomlock2] = activity1
            score_swap = scorefunction(schedule_swap, rooms, courses)

            if simulated_annealing_true == True:
                title_plot = 'Simulated Annealing'
                swaps_number += 1
                if swaps_number == 1000:
                    temp = temp * 0.75
                    swaps_number = 0
                    if temp < 1:
                        return schedule

                schedule = simulated_annealing(schedule, schedule_swap, temp, score_current, score_swap)
                score_now =  scorefunction(schedule, rooms, courses)

                if score_now < score_save:
                    score_save = score_now
                    schedule_save = schedule

                temp_number =+ 1

                score_plot_list.append(scorefunction(schedule, rooms, courses))


            else:
                title_plot = 'Hillclimber'
                schedule = hillclimber(schedule, schedule_swap, score_current, score_swap)
                schedule_save = schedule

                score_plot_list.append(scorefunction(schedule_save, rooms, courses))

    plot_scores(score_plot_list, number_iterations, title_plot)

    return schedule_save

def random_numbers():
    """"
    This function returns a random daylock, timelock and roomlock

    This function has no input arguments

    This function works as follows:
    - A daylock and timelock are randomly chosen
    - Given the timelock the roomlock is 0 or also randomly chosen
    """

    daylock = random.randint(0, 4)
    timelock = random.randint(0, 4)

    if timelock == 4:
        roomlock = 0
    else:
        roomlock = random.randint(0, 6)

    return [daylock, timelock, roomlock]

def hard_constraints(schedule_swap, overlap_dict, activity1, activity2, daylock1, daylock2, timelock1, timelock2, roomlock1, roomlock2):
    """
    This function checks if the hard constraint when swapping are satisfied

    - First is of the first acitity in the second roomlock checked if there is no overlapping
    - Then the order is checked of the first acitivity
    - Both actions are then also done for the second activity
    - If all the hard constraints are satisfied return True, otherwise return False
    """

    if overlapping(activity1, schedule_swap[daylock2][timelock2], overlap_dict):
        if order(schedule_swap, activity1, daylock2, timelock2):
            schedule_swap[daylock2][timelock2][roomlock2] = activity1
            if overlapping(activity2, schedule_swap[daylock1][timelock1], overlap_dict):
                if order(schedule_swap, activity2, daylock1, timelock1):
                    schedule_swap[daylock1][timelock1][roomlock1] = activity2
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def simulated_annealing(schedule, schedule_swap, temp, score_current, score_swap):

    """"
    Simulated annealing determines if swapped and returns correct schedule

    This function takes as input arguments:
    - schedule
    - schedule_swap
    - temperature
    - score_current
    - score_swap

    This function works as follows:
    - Of all both scores the e-score is calculated and added to e_score_sum.
    - A float between 0 and 1 is extracted from the uniform distribution (probability)
    - Calculate the probaility of choosing the current schedule (probability current)
    - If probability current is bigger than the probability from the unifrom distribution,
      the activities won't be swapped and current schedule is returned
    - Else, the activities are swapped by returning the swap schedule
    """
    e_score_current = math.exp(-score_current / temp)
    e_score_swap = math.exp(-score_swap / temp)
    e_score_sum = e_score_current + e_score_swap

    probability = random.uniform(0,1)
    prob_current = e_score_current / e_score_sum
    prob_swap = e_score_swap / e_score_sum


    if prob_current > probability:
        return schedule

    else:
        return schedule_swap

def hillclimber(schedule, schedule_swap, score_current, score_swap):
    """
    This algorithm determines if swapped and returns the correct schedule

    This function takes as input arguments:
    - schedule
    - schedule_swap
    - score_current
    - score_swap§

    This function works as follows:
    - If the current score is lower, no swap takes place and current schedule is returned
    - Else, the activities are swapped by returning the swap schedule
    """
    if score_current < score_swap:
        return schedule
    else:
        return schedule_swap
