from code.constraints.capacity import capacity
from code.constraints.overlap_simulated import overlapping
from code.constraints.order import order
import time

def scorefunction2(schedule, course_list, course_list_courses, rooms, overlap_dict):

    malus = 0;
    dict = {}

    for i in range(len(course_list)):
        dict[course_list[i]] = 0

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            for k in range(len(schedule[i][j])):
                if schedule[i][j][k] != None:
                    if j == 4:
                        malus = malus + 20
                # start_time = time.time()
                dict[schedule[i][j][k]] = int(dict[schedule[i][j][k]]) + int(1)
                malus = malus + capacity(schedule[i][j][k], rooms[k], course_list_courses)
                # print("--- %s seconds capacity ---" % (time.time() - start_time))
                if overlapping(schedule[i][j][k], schedule[i][j], overlap_dict) == False:
                    malus = malus + 800
                # print("--- %s seconds open_overlapping ---" % (time.time() - start_time))
                if order(schedule, schedule[i][j][k], i, j) == False:
                    malus = malus + 600
                # print("--- %s seconds order ---" % (time.time() - start_time))



    for i in range(len(course_list)):
        if course_list[i] is not None:
            number = dict[course_list[i]]
            course, sort = course_list[i].split('_')
            for i in range(len(course_list_courses)):
                if course_list_courses[i].name == course:
                    if 'lec' in sort:
                        number2 = int(course_list_courses[i].lec)
                        malus = malus + abs(number-number2)*1000
                    elif 'tut' in sort:
                        number2 = int(course_list_courses[i].tut_tot)
                        malus = malus + abs(number-number2)*1000

                    elif 'prac' in sort:
                        number2 = int(course_list_courses[i].prac_tot)
                        malus = malus + abs(number-number2)*1000


    return malus
