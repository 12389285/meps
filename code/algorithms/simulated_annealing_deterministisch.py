import random
import copy
import time
import math
from code.constraints.queue import alphabetic_queue
from code.algorithms.scorefunction2 import scorefunction2

def simulated_annealing_deterministisch(courses, schedule, rooms, overlap_dict):

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

    malus = scorefunction2(schedule, courses, rooms, overlap_dict)
    schedule_save = copy.deepcopy(schedule)
    # print(schedule)
    score_save = 1000000
    temp = 500
    for bigloop in range(2):
        temp = temp * 0.75
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    list_scores = []
                    e_score_sum = 0
                    new = 0
                    tmp2 = 0
                    array_a = []
                    array_b = []
                    array_c = []
                    for a in range(len(schedule)):
                        for b in range(len(schedule[a])):
                            for c in range(len(schedule[a][b])):
                                schedule_copy = copy.deepcopy(schedule)
                                schedule_copy[i][j][k] = schedule[a][b][c]
                                schedule_copy[a][b][c] = schedule[i][j][k]
                                score = scorefunction2(schedule_copy, courses, rooms, overlap_dict)
                                list_scores.append(score)
                                array_a.append(a)
                                array_b.append(b)
                                array_c.append(c)
                    min_score = min(list_scores)
                    e_scores = []
                    for z in range(len(list_scores)):
                        list_scores[z] = list_scores[z] - min_score
                        tmp = -list_scores[z]/temp
                        if tmp > 100:
                            tmp=100
                        e_score = math.exp(tmp)
                        e_scores.append(e_score)
                        e_score_sum = e_score_sum + e_score
                    # print(list_scores)
                    probability = random.uniform(0,1)
                    p_sum = 0
                    sum = 0
                    for m in range(len(e_scores)):
                        e_scores[m] = e_scores[m]/ e_score_sum
                        sum = sum + e_scores[m]
                        p_sum = p_sum + e_scores[m]
                        if p_sum > probability:
                            new = m
                            break

                    a = array_a[new]
                    b = array_b[new]
                    c = array_c[new]
                    temporary = schedule[i][j][k]
                    schedule[i][j][k] = schedule[a][b][c]
                    schedule[a][b][c] = temporary
                    score_check = scorefunction2(schedule, courses, rooms, overlap_dict)
                    if score_check < score_save:
                        score_save = score_check
                        schedule_save = schedule
                    print(bigloop)
                    print(f"scorecheck: ", score_check)
                    print(f"scoresave: ", score_save)
                    list_scores = []
                    e_scores = []

    return schedule_save
