import random
import copy
import time
import math
from code.algorithms.start_schedule_algorithm import alphabetic_queue
from code.algorithms.scorefunction_deterministic import scorefunction_deterministic

def make_random_schedule(courses, schedule, rooms, overlap_dict):
    """
    This function makes a random schedule (no hard constraints satisfied)

    This function takes as input arguments:
        - the courselist (classes)
        - the empty schedule
        - the roomlist
        - the overlapping dictionary

    This function works as follows:
    - It makes a alphabetical courselist (by calling the alphabetic_queue function)
    - It iterates over every roomlock in the empty schedule, at each empty roomlock it places a random course acitivty.
    - Then it removes the chosen acitivy from the courselist.
    This proces is repeated untill the courselist is empty.
    """

    course_list_alphabetic = alphabetic_queue(courses)

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            for k in range(len(schedule[i][j])):
                if course_list_alphabetic != []:
                    length = len(course_list_alphabetic)
                    list_place = random.randint(0, (length - 1))
                    schedule[i][j][k] = course_list_alphabetic[list_place]
                    course_list_alphabetic.remove(course_list_alphabetic[list_place])
    return schedule


def algorithm(courses, schedule_empty, iterations, rooms, overlap_dict, simulated_annealing_true):
    """
    This algorithm runs the deterministic algorithms

    This algorithm takes as input arguments:
    - the courselist (classes)
    - the empty schedule
    - number of iterations
    - the roomlist,
    - the overlapping dictionary
    - boolean for Simulated Annealing or Hillclimber (boolean)

    This function works as follows:
    - First a random schedule is made by calling the function make_random_schedule.
    - The score of the random schedule is saved, a copy of the schedule is made and the temperature is set.

    - The algorithm is run as many times as instructed by the user.
    - Every loop the temperature drops with a certain amount (only needed in the simulated annealing).
    - The algorithm iterates through every roomlock in the schedule (first),
    - At this roomlock (chosen by first iteration), the algorithm iterates again through the entire schedule
      and at every roomlock it swaps it with the roomlock of the first iteration.
    - Of every swap (175 for each roomlock in the first iteration), the score is calculated and put in list_scores
    - The daylock, roomlock and timelock indexes of each swap are put in a list,
      so when the swap is determined, the appurtenant activity can be found.

    - If the user instructed simulated annealing: the simulated annealing function determines the index of swap.
    - The swap function swaps with the chosen swap index.
    - If the swap has a better score then the saved score (at simulated annealing not always the case),
      this score and this schedule are saved

    - When the user instructed hillclimber: the hillclimber function determines the index of swap.
    - The swap function swaps with the chosen swap index.
    - Then the score is printed.
    """
    schedule = make_random_schedule(courses, schedule_empty, rooms, overlap_dict)
    score_save = scorefunction_deterministic(schedule, courses, rooms, overlap_dict)
    schedule_save = copy.deepcopy(schedule)
    temp = 150

    for bigloop in range(iterations):
        temp = temp * 0.75
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    list_scores = []
                    array_day = []
                    array_timelock = []
                    array_roomlock = []

                    for a in range(len(schedule)):
                        for b in range(len(schedule[a])):
                            for c in range(len(schedule[a][b])):
                                schedule_copy = copy.deepcopy(schedule)
                                schedule_copy[i][j][k] = schedule[a][b][c]
                                schedule_copy[a][b][c] = schedule[i][j][k]
                                score = scorefunction_deterministic(schedule_copy, courses, rooms, overlap_dict)
                                list_scores.append(score)

                                array_day.append(a)
                                array_timelock.append(b)
                                array_roomlock.append(c)

                    if simulated_annealing_true == True:
                        chosen_swap = simulated_annealing(list_scores, temp)
                        schedule = swap(schedule, chosen_swap, array_day, array_timelock, array_roomlock, i, j, k)

                        malus = score = scorefunction_deterministic(schedule, courses, rooms, overlap_dict)

                        if malus < score_save:
                            score_save = malus
                            schedule_save = schedule

                        # print(bigloop)
                        # print(f"scorecheck: ", malus)
                        # print(f"scoresave: ", score_save)

                    else:
                        score_current = scorefunction_deterministic(schedule, courses, rooms, overlap_dict)
                        chosen_swap = hillclimber(list_scores, score_current)
                        if chosen_swap != False:
                            schedule = swap(schedule, chosen_swap, array_day, array_timelock, array_roomlock, i, j, k)
                        malus = scorefunction_deterministic(schedule, courses, rooms, overlap_dict)
                        # print(f"score: ", malus)

    return schedule

def hillclimber(list_scores, score):

    """
    Hillclimber determines the swap

    This function takes as input arguments:
    - list_scores
    - current score of unswapped schedule

    This function works as follows:
    - The minimum of scorelist is determined
    - If the minimum score is lower than the current score:
      The minimum score is looked up in the score list and the corresponding index number is returned
    - Else, False is returned
    """

    min_score = min(list_scores)

    if min_score < score:
        for m in range(len(list_scores)):
            if list_scores[m] == min_score:
                return m
    else:
        return False


def simulated_annealing(list_scores, temp):
    """
    Simulated annealing determines the swap

    This function takes as input arguments:
    - list_scores
    - current score of unswapped schedule

    This function works as follows:
    - The minimum of scorelist is determined
    - If the minimum score is lower than the current score:
      The minimum score is looked up in the score list and the corresponding index number is returned
    - Else, False is returned
    """

    e_scores = []
    e_score_sum = 0
    min_score = min(list_scores)
    for z in range(len(list_scores)):
        list_scores[z] = list_scores[z] - min_score
        tmp = -list_scores[z]/temp
        if tmp > 100:
            tmp=100
        e_score = math.exp(tmp)
        e_scores.append(e_score)
        e_score_sum = e_score_sum + e_score

    probability = random.uniform(0,1)
    p_sum = 0

    for n in range(len(e_scores)):
        e_scores[n] = e_scores[n]/ e_score_sum
        p_sum = p_sum + e_scores[n]
        if p_sum > probability:
            return n


def swap(schedule, chosen_swap, array_day, array_timelock, array_roomlock, i, j, k):
    a = array_day[chosen_swap]
    b = array_timelock[chosen_swap]
    c = array_roomlock[chosen_swap]

    temporary = schedule[i][j][k]
    schedule[i][j][k] = schedule[a][b][c]
    schedule[a][b][c] = temporary

    return schedule
