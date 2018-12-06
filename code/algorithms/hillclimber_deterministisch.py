import random
import copy
import time
import math
from code.constraints.queue import alphabetic_queue
from code.algorithms.scorefunction2 import scorefunction2

def hillclimber_determin(courses, schedule, rooms, overlap_dict):

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

    score = scorefunction2(schedule, courses, rooms, overlap_dict)

    # print(schedule)
    for bigloop in range(10):
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                for k in range(len(schedule[i][j])):
                    list_scores = []
                    new = 0
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
                    if min_score < score:
                        for z in range(len(list_scores)):
                            if list_scores[z] == min_score:
                                new = z
                                break
                        score = min_score
                        a = array_a[new]
                        b = array_b[new]
                        c = array_c[new]
                        temporary = schedule[i][j][k]
                        schedule[i][j][k] = schedule[a][b][c]
                        schedule[a][b][c] = temporary
                        print(bigloop)
                        print(f"score: ", score )


    return schedule_save
