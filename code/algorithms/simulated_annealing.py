import random
import copy
import time
import math

from code.algorithms.scorefunction2 import scorefunction2

def simulated_annealing(course_list, schedule, course_list_simulated, rooms, overlap_dict):

    course_list_simulated.append(None)
    length = len(course_list_simulated)

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            for k in range(len(schedule[i][j])):
                schedule[i][j][k] = course_list_simulated[random.randint(0, (length - 1))]


    malus = scorefunction2(schedule, course_list_simulated, course_list, rooms, overlap_dict)
    schedule_save = copy.deepcopy(schedule)
    # print(schedule)
    score_save = 1000000
    temp = 750
    for bigloop in range(10):
        temp = temp * 0.75
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    list_scores = []
                    e_score_sum = 0
                    new = 0
                    tmp2 = 0
                    schedule_copy = copy.deepcopy(schedule)
                    for l in range(len(course_list_simulated)):
                        schedule_copy[i][j][k] = course_list_simulated[l]
                        score = scorefunction2(schedule_copy, course_list_simulated, course_list, rooms, overlap_dict)
                        list_scores.append(score)
                    array_a = []
                    array_b = []
                    array_c = []
                    check = []
                    for a in range(len(schedule)):
                        for b in range(len(schedule[a])):
                            for c in range(len(schedule[a][b])):
                                schedule_copy2 = copy.deepcopy(schedule)
                                schedule_copy2[i][j][k] = schedule[a][b][c]
                                schedule_copy2[a][b][c] = schedule[i][j][k]
                                score2 = scorefunction2(schedule_copy2, course_list_simulated, course_list, rooms, overlap_dict)
                                list_scores.append(score2)
                                check.append(score2)
                                array_a.append(a)
                                array_b.append(b)
                                array_c.append(c)
                    min_score = min(list_scores)
                    e_scores = []
                    for z in range(len(list_scores)):
                        list_scores[z] = list_scores[z] - min_score
                        tmp2 = -list_scores[z]/temp
                        if tmp2 > 100:
                            tmp2=100
                        e_score = math.exp(tmp2)
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

                    if new < len(course_list_simulated):
                        schedule[i][j][k] = course_list_simulated[new]
                    else:
                        print('swap')
                        new = new - len(course_list_simulated)
                        a = array_a[new]
                        b = array_b[new]
                        c = array_c[new]
                        temporary = schedule[i][j][k]
                        schedule[i][j][k] = schedule[a][b][c]
                        schedule[a][b][c] = temporary
                    score_check = scorefunction2(schedule, course_list_simulated, course_list, rooms, overlap_dict)
                    if score_check < score_save:
                        score_save = score_check
                        schedule_save = schedule
                    print(bigloop)
                    print(f"scorecheck: ", score_check)
                    print(f"scoresave: ", score_save)
                    list_scores = []
                    e_scores = []

    print(schedule_save)
