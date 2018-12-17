import random
import copy
import time
import math
from code.algorithms.start_schedule_algorithm import alphabetic_queue
from code.algorithms.scorefunction_deterministic import scorefunction_deterministic


def make_random_schedule(courses, schedule, rooms, overlap_dict):

    course_list_alphabetic = alphabetic_queue(courses)
    print(course_list_alphabetic)

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            for k in range(len(schedule[i][j])):
                if course_list_alphabetic != []:
                    length = len(course_list_alphabetic)
                    list_place = random.randint(0, (length - 1))
                    schedule[i][j][k] = course_list_alphabetic[list_place]
                    course_list_alphabetic.remove(course_list_alphabetic[list_place])
    return schedule


def algorithm(courses, schedule_2, iterations, rooms, overlap_dict, simulated_annealing_true):

    schedule = make_random_schedule(courses, schedule_2, rooms, overlap_dict)
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

                        print(bigloop)
                        print(f"scorecheck: ", malus)
                        print(f"scoresave: ", score_save)

                    else:
                        chosen_swap = hillclimber(list_scores, score)
                        if chosen_swap != False:
                            schedule = swap(schedule, chosen_swap, array_day, array_timelock, array_roomlock, i, j, k)
                        malus = score = scorefunction_deterministic(schedule, courses, rooms, overlap_dict)
                        print(bigloop)
                        print(f"score: ", malus)



    return schedule

def hillclimber(list_scores, score):
    min_score = min(list_scores)

    if min_score < score:
        for m in range(len(list_scores)):
            if list_scores[m] == min_score:
                return m
    else:
        return False


def simulated_annealing(list_scores, temp):

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
